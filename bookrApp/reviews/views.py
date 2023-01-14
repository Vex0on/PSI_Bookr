from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone

from .models import Book, Publisher, Contributor, Review
from .utils import average_rating
from .forms import SearchForm, PublisherForm, ReviewForm


def welcome_view(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("szukaj", "")
    form = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["szukaj"]:
        szukaj = form.cleaned_data["szukaj"]
        szukaj_w = form.cleaned_data.get("szukaj_w") or "tytuł"
        if szukaj_w == "tytuł":
            books = Book.objects.filter(title__icontains=szukaj)
        elif szukaj_w == "współtwórca":
            books = Book.objects.filter(
                Q(contributors__first_names__icontains=szukaj) | Q(contributors__last_names__icontains=szukaj)).distinct()
    return render(request, "search-results.html", {"form": form, "search_text": search_text, "books": books})


def book_list(request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
        context = {
            'book_list': book_list
        }
    return render(request, 'book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, "book_detail.html", context)


def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None

    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Wydawca \"{}\" został utworzony.".format(updated_publisher))
            else:
                messages.success(request, "Wydawca \"{}\" został zaktualizowany.".format(updated_publisher))

            return redirect("publisher_edit", updated_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)

    return render(request, "instance-form.html",
                  {"form": form, "instance": publisher, "model_type": "Publisher"})


def review_edit(request, book_pk, review_pk=None):
    book = get_object_or_404(Book, pk=book_pk)

    if review_pk is not None:
        review = get_object_or_404(Review, book_id=book_pk, pk=review_pk)
    else:
        review = None

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            updated_review = form.save(False)
            updated_review.book = book

            if review is None:
                messages.success(request, "Recenzja \"{}\" utworzona.".format(book))
            else:
                updated_review.date_edited = timezone.now()
                messages.success(request, "Recenzja \"{}\" zaktualizowana.".format(book))

            updated_review.save()
            return redirect("book_detail", book.pk)

    else:
        form = ReviewForm(instance=review)

    return render(request, "instance-form.html",
                  {"form": form,
                   "instance": review,
                   "model_type": "Review",
                   "related_instance": book,
                   "related_model_type": "Book"
                   })

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})

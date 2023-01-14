from django import forms
from .models import Publisher, Review


class SearchForm(forms.Form):
    szukaj = forms.CharField(required=False, min_length=3)
    szukaj_w = forms.ChoiceField(required=False, choices=(
        ("tytuł", "Tytuł"),
        ("współtwórca", "Współtwórca")
    ))


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)

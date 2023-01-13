from django import forms


class SearchForm(forms.Form):
    szukaj = forms.CharField(required=False, min_length=3)
    szukaj_w = forms.ChoiceField(required=False, choices=(
        ("tytuł", "Tytuł"),
        ("współtwórca", "Współtwórca")
    ))

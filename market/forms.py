from django.forms import ModelForm, Form
from django import forms
from dal import autocomplete

from .models import Stock, Price

class SearchForm(Form):
    stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        widget=autocomplete.ModelSelect2(url='market:stock-autocomplete')
    )
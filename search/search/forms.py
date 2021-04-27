from django import forms

class SearchForm(forms.Form):
    category = forms.CharField(label='category',max_length=20)
    search_keyword = forms.CharField(label='search_keyword', max_length=20)
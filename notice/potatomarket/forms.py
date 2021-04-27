from django import forms
from django.db import models
from potatomarket.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_title', 'item_price', 'item_detail','item_category']

from django.contrib import admin
from potatomarket.models import Item


class ItemAdmin(admin.ModelAdmin):
    #fields = ['item_name', 'item_views', 'item_price', 'item_status', 'item_date']
    pass


admin.site.register(Item, ItemAdmin)

import json
import os
from datetime import datetime

import elasticsearch
import consul
import jwt
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import logging
from django.views.generic import ListView
from elasticsearch import Elasticsearch

from .settings import JWT_SECRET_KEY
from .models import Item
from django.views.generic import CreateView
from .forms import ItemForm

logger = logging.getLogger(__name__)

client = consul.Consul(host='172.19.0.100', port=8500)

home = "http://{}:{}/".format(client.catalog.service("main")[1][0]['Address'],
                              client.catalog.service("main")[1][0]['ServicePort'])
signin = "http://{}:{}/signin/".format(client.catalog.service("sign")[1][0]['Address'],
                                       client.catalog.service("sign")[1][0]['ServicePort'])
item_link = "http://{}:{}/items/".format(client.catalog.service("itemDetail")[1][0]['Address'],
                                         client.catalog.service("itemDetail")[1][0]['ServicePort'])
user_link = "http://{}:{}/user_detail/".format(client.catalog.service("userDetail")[1][0]['Address'],
                                               client.catalog.service("userDetail")[1][0]['ServicePort'])
search = "http://{}:{}/search/".format(client.catalog.service("search")[1][0]['Address'],
                                       client.catalog.service("search")[1][0]['ServicePort'])


# home = 'http://127.0.0.1:8001/'
# signin = 'http://127.0.0.1:8002/signin/'
# item_link = 'http://127.0.0.1:8003/items/'
# user_link = 'http://127.0.0.1:8004/user/'
# search = 'http://127.0.0.1:8006/search'

# Create your views here.

def logout(request):
    response = HttpResponseRedirect(home)
    response.delete_cookie('TOKEN')
    return response


class ItemLV(ListView):
    model = Item
    template_name = 'potatomarket/index.html'
    context_object_name = 'items'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        link = super(ItemLV, self).get_context_data(**kwargs)
        link['home'] = home
        link['signin'] = signin
        link['item_link'] = item_link
        link['user_link'] = user_link
        link['search'] = search
        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
        else:
            token = ""
        # print(self.response.headers['Location'])
        link['token'] = token
        return link


class ClothesItemLV(ItemLV):
    def get_queryset(self):
        return self.model.objects.filter(item_category="clothes")


class DeviceItemLV(ItemLV):
    def get_queryset(self):
        return self.model.objects.filter(item_category="device")


class FurnitureItemLV(ItemLV):
    def get_queryset(self):
        return self.model.objects.filter(item_category="furniture")


class ItemCreateView(CreateView):
    template_name = 'potatomarket/add_item.html'
    success_url = '/'  # 1
    form_class = ItemForm  # 2

    def form_valid(self, form):
        form.instance.user = self.request.user
        logger.debug("'item_name': {}, 'item_price': {}, 'item_detail': {}".format(self.request.POST.get('item_name'),
                                                                                   self.request.POST.get('item_price'),
                                                                                   self.request.POST.get(
                                                                                       'item_detail')))

        token = self.request.COOKIES['TOKEN']
        user_no = jwt.decode(token, JWT_SECRET_KEY, algorithm='HS256')
        form.instance.user_no = user_no['user']

        # es = Elasticsearch('[엘라스틱_서버_IP_주소]:9200')
        #
        # doc = {"item_category": self.request.POST.get('item_category'),
        #        "item_date": datetime.now(),
        #        "item_detail": self.request.POST.get('item_detail'),
        #        "item_price": self.request.POST.get('item_name'),
        #        "item_statue": "판매중",
        #        "item_title": self.request.POST.get('item_title'),
        #        }
        #
        # res = es.index(index="auto_complete3", doc_type="_doc", body=doc)
        # print(res)

        return super(ItemCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):

        link = super(ItemCreateView, self).get_context_data(**kwargs)
        link['home'] = home
        link['signin'] = signin
        link['item_link'] = item_link
        link['user_link'] = user_link
        link['search'] = search
        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
        else:
            token = ""
        # print(self.response.headers['Location'])
        link['token'] = token
        return link

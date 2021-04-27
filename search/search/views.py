import consul
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from search.forms import SearchForm
from search.es import search_category

import os
from random import randint

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

link = {'home': home, 'signin': signin, 'item_link': item_link, 'user_link': user_link, 'search': search};


def logout(request):
    response = HttpResponseRedirect(home)
    response.delete_cookie('TOKEN')
    return response


def search(request):
    result = []

    if 'TOKEN' in request.COOKIES:
        token = request.COOKIES['TOKEN']
    else:
        token = ""
    link['token'] = token

    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']
            search_keyword = form.cleaned_data['search_keyword']

            if category:
                result = search_category(category, search_keyword)

        return render(request, 'search/index.html', {'result': result, 'link': link})
    else:
        form = SearchForm()
    return render(request, 'search/index.html', {'link': link})

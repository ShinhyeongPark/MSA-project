from collections import namedtuple

import consul
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
import os

from django.shortcuts import render, redirect

import jwt
import json
import requests
from mysite.settings import JWT_SECRET_KEY

client = consul.Consul(host='172.19.0.100', port=8500)

home = "http://{}:{}/".format(client.catalog.service("main")[1][0]['Address'],
                              client.catalog.service("main")[1][0]['ServicePort'])
signin = "http://{}:{}/signin/".format(client.catalog.service("sign")[1][0]['Address'],
                                       client.catalog.service("sign")[1][0]['ServicePort'])

item_link = "http://{}:{}/items/".format(client.catalog.service("itemDetail")[1][0]['Address'],
                                         client.catalog.service("itemDetail")[1][0]['ServicePort'])
user_link = "http://{}:{}/user_detail/".format(client.catalog.service("userDetail")[1][0]['Address'],
                                               client.catalog.service("userDetail")[1][0]['ServicePort'])
user_api = "http://{}:{}/".format(client.catalog.service("userapi")[1][0]['Address'],
                                  client.catalog.service("userapi")[1][0]['ServicePort'])
search = "http://{}:{}/search/".format(client.catalog.service("search")[1][0]['Address'],
                                       client.catalog.service("search")[1][0]['ServicePort'])
print(user_api)
# home = 'http://127.0.0.1:8001/'
# signin = 'http://127.0.0.1:8002/signin/'
# item_link = 'http://127.0.0.1:8003/items/'
# user_link = 'http://127.0.0.1:8004/user/'
user_api = 'http://172.19.0.8:8000/'
# search = 'http://127.0.0.1:8006/search'

link = {'home': home, 'signin': signin, 'item_link': item_link, 'user_link': user_link, 'user_api': user_api,
        'search': search}


def logout(request):
    response = HttpResponseRedirect(home)
    response.delete_cookie('TOKEN')
    return response


class userDV(DetailView):
    model = User
    template_name = "user/index.html"

    def get_object(self):
        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
            user_no = jwt.decode(token, JWT_SECRET_KEY, algorithm='HS256')
            url = user_api + 'user_detail'
            # get
            headers = {'Content-type': 'application/json'}
            data = {"userno": user_no}
            r = requests.get(url, headers=headers, data=json.dumps(data))
            print(r.text)
            print(type(r.text))  # str
            a = json.loads(r.text)  # json

            user_detail = namedtuple("UserDetail", a.keys())(*a.values())  # json -> obj

            return user_detail  # obj

        else:
            print(signin)
            return redirect('http://www.naver.com')

    def get_context_data(self, **kwargs):
        link = super(userDV, self).get_context_data(**kwargs)
        link['home'] = home
        link['signin'] = signin
        link['item_link'] = item_link
        link['user_link'] = user_link
        link['search'] = search
        if 'TOKEN' in self.request.COOKIES:
            token = self.request.COOKIES['TOKEN']
        else:
            token = ""
        link['token'] = token
        return link

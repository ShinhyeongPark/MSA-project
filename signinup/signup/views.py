import jwt
import consul
import json
import bcrypt
import requests

from .models import User
from django.views import View
from datetime import datetime
from django.contrib import auth
from rest_framework_jwt.settings import api_settings
from django.shortcuts import render, redirect
from potato.settings import SECRET_KEY
from django.http import HttpResponse, JsonResponse  # HTTP 통신
from django.contrib import messages
from rest_framework import status

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

# home = 'http://127.0.0.1:8001/'
# signin = 'http://127.0.0.1:8002/signin/'
# item_link = 'http://127.0.0.1:8003/items/'
# user_link = 'http://127.0.0.1:8004/user/'
user_api = 'http://172.19.0.8:8000/'

link = {'home': home, 'signin': signin, 'item_link': item_link, 'user_link': user_link, 'user_api': user_api};


def index(request):
    return render(request, 'main/register.html', {'link': link})


def signup(request):
    if request.method == "POST":
        try:
            # if User.objects.filter(user_email=request.POST['user_email']).exists():  # 중복이 되면 안되는 항목
            #     messages.info(request, '이미 존재하는 Email입니다.')
            #     return redirect('./')
            #     # return JsonResponse({'message' : 'Aleady Exist Email'}, status=400)
            # elif User.objects.filter(user_nickname=request.POST['user_nickname']).exists():  # 중복이 되면 안되는 항목
            #     messages.info(request, '이미 존재하는 Nickname입니다.')
            #     return redirect('./')
            #     # return JsonResponse({'message' : 'Aleady nickname Email'}, status=400)
            #
            # # Email과 nickname이 중복되지 않았을 경우
            # User.objects.create(
            #     user_email=request.POST['user_email'],
            #     user_password=bcrypt.hashpw(request.POST['user_password'].encode("UTF-8"), bcrypt.gensalt()).decode(
            #         "UTF-8"),
            #     user_nickname=request.POST['user_nickname'],
            #     user_location=request.POST['user_location'],
            #     user_gender=request.POST['user_gender'],
            #     user_birthdate=request.POST['user_birthdate']
            # ).save()
            response = requests.post(user_api + 'user', data=request.POST)

            print(response.status_code)
            if response.status_code == status.HTTP_400_BAD_REQUEST:
                messages.info(request, '이미 존재하는 Email/nickname입니다.')
            return redirect(link['signin'])
            # return HttpResponse(status = 200)

        except KeyError:
            return redirect('./')
            # return JsonResponse({'message' : 'Invalid Key'}, status=400)


def get(request):
    userData = User.objects.values()
    return JsonResponse({'member': list(userData)}, status=200)


def loginpage(request):
    return render(request, 'main/login.html', {'link': link})


def login(request):
    # POST 요청이 들어올 경우
    if request.method == "POST":
        try:
            # # 입력된 Email이 DB에 존재한다면
            # # Email이 유효
            # if User.objects.filter(user_email=request.POST['user_email']).exists():
            #     user = User.objects.get(user_email=request.POST['user_email'])
            #     # 비밀번호(암호화된)를 비교
            #     # 비밀번호도 유효할 경우
            #     # 로그인 성공 + 토큰 발급
            #     if bcrypt.checkpw(request.POST['user_password'].encode("UTF-8"), user.user_password.encode("UTF-8")):
            #         token = jwt.encode({'user': user.user_no}, SECRET_KEY, algorithm='HS256').decode('UTF-8')
            #         # return JsonResponse({'token': token, 'user':user.user_no}, status = 200)
            #
            #         # print(request)
            #         # request['token'] = token
            #         response = redirect(link['home'], {'TOKEN': token})
            #         response['TOKEN'] = token
            #         response.set_cookie('TOKEN', token)
            #         return response
            response = requests.post(user_api + 'login', data=request.POST)
            if response.status_code == status.HTTP_200_OK:
                token = response.json()['token']
                response = redirect(link['home'], {'TOKEN': token})
                response['TOKEN'] = token
                response.set_cookie('TOKEN', token)
                return response

            else:
                # return redirect(link['home'], token=token)
                # 예외처리: Password 오류
                messages.info(request, '1.Email 또는 Password가 틀렸습니다.')
                return redirect('./', {'error': 'username or password is incorrect'})
                # return HttpResponse(status = 401)
            # 예외처리: 존재하지 않는 Email
            messages.info(request, '2.Email 또는 Password가 틀렸습니다.')
            return redirect('./', {'error': 'username or password is incorrect'})
            # return HttpResponse(status= 400)

        except KeyError:
            messages.info(request, '3.Email 또는 Password가 틀렸습니다.')
            return redirect('./', {'error': 'username or password is incorrect'})
            # return render(request, 'signin/', {'error':'username or password is incorrect'})
            # return JsonResponse({'message : Invalid Key'}, status = 400)

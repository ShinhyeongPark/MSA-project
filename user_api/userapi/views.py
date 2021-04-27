from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
import os
from django.http import JsonResponse
from rest_framework.views import APIView
import jwt
import bcrypt
from .settings import JWT_SECRET_KEY
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailViewSet(APIView):

    def get(self, request, format=None):

        # if 'TOKEN' in self.request.COOKIES:
        # print(request.COOKIES)
        # print('hello')
        # token = self.request.COOKIES['TOKEN']
        # user_no = jwt.decode(token, JWT_SECRET_KEY, algorithm='HS256')
        # print(user_no)
        if 'user' in self.request.data['userno']:
            user_no = self.request.data['userno']['user']
            print(user_no)
            user = User.objects.get(user_no=user_no)
            # print(user)
            return JsonResponse({'user': user_no, 'user_email': user.user_email, 'user_nickname': user.user_nickname,
                                 'user_gender': user.user_gender, 'user_birthdate': user.user_birthdate}, status=200)

        else:
            return JsonResponse({'error': 'Email 또는 Password가 틀렸습니다.'}, status=403)

        # user = User.objects.filter(user_no='user_no')
        # serializer = UserSerializer(user, many=True)
        # return Response(serializer.data)

        # print(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     print('hi2213')
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    # if 'TOKEN' in self.request.COOKIES:
    #     token = self.request.COOKIES['TOKEN']
    #     user_no = jwt.decode(token, JWT_SECRET_KEY, algorithm='HS256')
    #     return self.model.objects.get(pk=user_no['user'])

    # else:
    #     print(signin)
    #     return redirect('http://www.naver.com')


class LoginViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():

            # 입력된 Email이 DB에 존재한다면
            # Email이 유효
            if User.objects.filter(user_email=request.data['user_email']).exists():
                user = User.objects.get(user_email=request.data['user_email'])
                # 비밀번호(암호화된)를 비교
                # 비밀번호도 유효할 경우
                # 로그인 성공 + 토큰 발급
                if bcrypt.checkpw(request.data['user_password'].encode("UTF-8"), user.user_password.encode("UTF-8")):
                    token = jwt.encode({'user': user.user_no}, JWT_SECRET_KEY, algorithm='HS256').decode('UTF-8')
                    print(token)
                    return JsonResponse({'token': token, 'user': user.user_no}, status=200)

                else:
                    # 예외처리: Password 오류
                    return JsonResponse({'error': 'Email 또는 Password가 틀렸습니다.'}, status=403)

            else:
                return JsonResponse({'error': 'Email 또는 Password가 틀렸습니다.'}, status=403)

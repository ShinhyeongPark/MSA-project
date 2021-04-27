from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from . import views

# app_name = 'signin'
urlpatterns = [
#localhost:8000/signin
    path('signin/', views.loginpage, name='index'), #로그인 화면
    #localhost:8000/signin/check
    path('signin/check', views.login, name='check'), #로그인 후 화면 (메인으로 이동)
    #localhost/signup
    path('signup/', views.index, name='index'), #회원가입 페이지
    #localhost/signup/check
    path('signup/check', views.signup, name='success'), #회원가입 성공 후 페이지
    #localhost/signup/list 
    path('signup/list', views.get) #회원가입된 사용자 목록
                                    #추후 삭제할 기능
]
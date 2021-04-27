from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet)


urlpatterns = [
    path('login', LoginViewSet.as_view()),
    path('user_detail',UserDetailViewSet.as_view()),
    path('', include(router.urls))
    ]


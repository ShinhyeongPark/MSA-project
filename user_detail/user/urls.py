from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', userDV.as_view(), name='user_detail')
]
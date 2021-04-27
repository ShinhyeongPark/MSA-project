"""items URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout, name='logout'),
    path('items/<int:product_no>/', views.item_detail, name='items_detail'),
    path('items/<int:product_no>/comment', views.comment_insert, name='comment_insert'),
    path('items/<int:product_no>/comment/<int:comment_no>', views.comment_detail, name='comment_detail'),
    path('items/<int:product_no>/comment/<int:comment_no>/update',views.comment_update, name='comment_update')
]
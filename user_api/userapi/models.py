from datetime import datetime

from django.db import models

#회원가입시 입력된 데이터를 저장한 테이블
#Table:  users
class User(models.Model):
    objects = models.Manager()
    # user_email = models.EmailField(max_length=100, unique=True)
    # user_password = models.CharField(max_length=20)
    # user_nickname = models.CharField(max_length=100, unique=True)
    # user_location = models.CharField(max_length=100,null=True)
    # user_gender = models.CharField(max_length=100,null=True)
    # user_birthdate = models.DateField(null=True)
    # user_createat = models.DateField(default=datetime.now)
    # user_caution = models.IntegerField(default=0)
    # user_sellcount = models.IntegerField(default=0)
    user_no = models.AutoField(primary_key=True)
    user_password = models.CharField(max_length=100)
    user_email = models.CharField(max_length=50)
    user_nickname = models.CharField(max_length=20)
    user_location = models.CharField(max_length=20)
    user_gender = models.CharField(max_length=20)
    user_birthdate = models.DateField(blank=True, null=True)
    user_createat = models.DateField(blank=True, null=True)
    user_caution = models.IntegerField(blank=True, null=True)
    user_sellcount = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user' #테이블명
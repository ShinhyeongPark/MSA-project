from .models import *
from rest_framework import serializers
import bcrypt
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['user_no','user_password','user_email','user_nickname','user_gender','user_birthdate']

    def validate(self,data):
        print('hi00')

        if User.objects.filter(user_email=data['user_email']).exists():  # 중복이 되면 안되는 항목
            raise serializers.ValidationError("이미 존재하는 email입니다.")

        elif User.objects.filter(user_nickname=data['user_nickname']).exists():  # 중복이 되면 안되는 항목
            raise serializers.ValidationError("이미 존재하는 nickname입니다.")

        return data

    def create(self,validated_data) :
        print('hi')
        print(validated_data)
        user = User(
            #user_no = validated_data['user_no'],
            user_password=bcrypt.hashpw(validated_data['user_password'].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8"),
            user_email = validated_data['user_email'],
            user_nickname = validated_data['user_nickname'],
            user_gender = validated_data['user_gender'],
            user_birthdate = validated_data['user_birthdate']
        )




        print(user)


        user.save()


        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['user_password','user_email']

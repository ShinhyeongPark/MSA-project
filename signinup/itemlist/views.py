#view파일: html을 연결 요청하는 파일

from django.shortcuts import render

def index(request): #현재디렉터리 templates
    return render(request,'main/index.html')
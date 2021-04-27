FROM python:3.7.9-stretch

RUN apt-get update
RUN pip install django
RUN pip install mysqlclient
RUN pip install djangorestframework djangorestframework-jwt
RUN pip install django-cognito-jwt
RUN apt-get install -y vim
RUN pip install bcrypt

WORKDIR /user_api
COPY /user_api /user_api


EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
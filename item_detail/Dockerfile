FROM python:3.7.9-stretch

RUN apt-get update
RUN pip install django
RUN pip install mysqlclient
RUN pip install python-consul
RUN apt-get install -y vim


WORKDIR /items_detail
COPY /item_detail /items_detail


EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]
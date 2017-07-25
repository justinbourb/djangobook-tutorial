#mysite\books\urls.py

from django.conf.urls import url
'''some you can import views instead of each individual view'''
from books import views

urlpatterns = [
    url(r'^search/$', views.search),
    ]

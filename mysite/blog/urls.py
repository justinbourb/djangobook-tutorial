from django.conf.urls import url
'''some you can import views instead of each individual view'''
from blog import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    ]

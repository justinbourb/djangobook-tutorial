"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#don't forget to imports view pages from views file!!!!!!!!!
from mysite.views import hello, my_homepage_view, current_datetime, hours_ahead, histowiz, display_meta, contact

''' url(r'^', include('books.urls')), must be last r'^' send everything to books.urls,
so we want to make sure none of the other patterns match before sending
django to check books/urls.py for matching patterns.'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #^matches beginning of RegEx, $ matches end
    url(r'^hello/$', hello),
    url(r'^$', my_homepage_view),
    url(r'^time/$', current_datetime),
    url(r'^another-time-page/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^histowiz/$', histowiz),
    url(r'^display_meta/$', display_meta),
    url(r'^contact/$', contact),
    url(r'^', include('books.urls')),
    url(r'^', include('blog.urls')),
    
]

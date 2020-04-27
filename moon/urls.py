# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.homepage),
    url(r'/create/new$',views.create_new),
    url(r'/persional$',views.peisional),
]

from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.login),
    url(r'^home',include('moon.urls'))
]

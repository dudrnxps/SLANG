from django.conf.urls import patterns, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

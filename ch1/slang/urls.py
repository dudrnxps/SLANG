from django.conf.urls import patterns, url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^slang/', include('chatting.urls', namespace='slang')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]

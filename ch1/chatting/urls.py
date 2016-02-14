from django.conf.urls import patterns, url
from chatting import views

urlpatterns = patterns('',
    url(r'^$',views.Index.as_view(),name="index"),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^teamCreate/$',views.Team_create.as_view(),name='teamCreate'),
    url(r'^teamEnter/$',views.Team_enter.as_view(), name='teamEnter'),
    url(r'^team/(?P<team_name>\w+)/$',views.Chat.as_view(),name='team'),
)

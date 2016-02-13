from django.conf.urls import patterns,url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from chatting import views
from chatting.forms import LoginForm

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name="chatting/index.html"),name="index"),
    url(r'^Signup/$',views.Signup.as_view(),name="Signup"),
    url(r'^login/$',views.login_view,name='login'),
    url(r'^teamCreate/$',views.Team_create.as_view(),name='teamCreate'),
    url(r'^teamEnter/$',views.Team_enter.as_view(), name='teamEnter'),
    url(r'^team/(?P<team_name>\w+)/$',views.Chat.as_view(),name='team'),
   
    
)

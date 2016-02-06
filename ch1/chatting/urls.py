from django.conf.urls import patterns,url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from chatting import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$',TemplateView.as_view(template_name="chatting/index.html"),name="index"),
    url(r'^Signup/$',views.Signup.as_view(),name="Signup"),
    url(r'^Login/$',TemplateView.as_view(template_name="chatting/Login.html"),name="Login"),
    url(r'^/$',TemplateView.as_view(template_name="js/cloud-carousel.1.0.5.js"),name="cloud-carousel"),
)

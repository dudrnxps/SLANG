from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, View
from django.views.generic.edit import FormView
from chatting.models import Membership, Team, File
from chatting.forms import SignupForm

# Create your views here.
class Signup(FormView):
    form_class = SignupForm
    success_url = "/"
    template_name = 'chatting/Signup.html'
    
    def post(self,request):
        mem_username = request.POST['username']
        mem_mail = request.POST['email']
        mem_pass = request.POST['password']
        membership = Membership(mem_username=mem_username,mem_mail=mem_mail,mem_pass=mem_pass)
        membership.save()
        
        return HttpResponseRedirect(reverse('slang:Signup'));

   
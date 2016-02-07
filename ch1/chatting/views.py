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
    
    def form_valid(self,form):
        self.mem_username=self.request.POST['username']
        self.mem_pass=self.request.POST['password']
        self.mem_mail=self.request.POST['email']
        return super(Signup,self).form_valid(form)
   
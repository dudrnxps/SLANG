from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import ListView, View
from chatting.models import Membership, Team, File
# Create your views here.

class Signup(View):
    def get(self,request):
            return render(request,'chatting/Signup.html')
    
    def post(self,request):
        form=(request.POST)
        if form.is_valid():
            membership.mem_username=request.username
            membership.mem_mail=request.email
            membership.mem_pass=request.password
            membership.save()
            return HttpResponseRedirect(reverse('chatting:index',args=()))
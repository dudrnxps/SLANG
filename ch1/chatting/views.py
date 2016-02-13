from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, View, TemplateView
from django.views.generic.edit import FormView
from chatting.models import Membership, Team, File
from chatting.forms import SignupForm,LoginForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        membership = form.login(request)
        if membership:
            login(request,membership)
            return HttpResponseRedirect(reverse('slang:signup'))
    return render(request,'chatting/Login.html',{'login_form':form})

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
        
        return HttpResponseRedirect(reverse('slang:login'));

class Team_create(TemplateView):
    template_name = "team/create.html"
    def post(self,request):
        name = request.POST['teamName']
        new_team = Team(team_name=name)
        new_team.save()
        return HttpResponseRedirect('/slang/teamEnter');

class Team_enter(TemplateView):
    template_name = "team/enter.html"
    def post(self,request):
        name = request.POST['teamName']
        try:
            checkName = Team.objects.get(team_name=name)
        except:
            return HttpResponse('fail')
        else:
            return HttpResponseRedirect('/slang/team/%s/' % name)
        
class Chat(TemplateView):
    template_name = "team/chat.html"

        
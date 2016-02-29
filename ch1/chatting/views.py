from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.views.generic import ListView, View, TemplateView
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.views.decorators.csrf import csrf_exempt
from chatting.forms import AuthenticationForm, RegistrationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from chatting.models import Member,Team
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect,requires_csrf_token
import json
from django.contrib.sessions.models import Session
from django.utils import timezone
from django import template


class Index(TemplateView):
    template_name = "chatting/index.html"
    
@csrf_exempt
def login(request):
    """
    Log in view
    """
    if request.method == 'POST' and request.is_ajax():
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            m = Member.objects.get(username=request.POST['username'])
            if user is not None:
                if user.is_active:
                    request.session['member_id']=m.id
                    request.session['member_name']=m.username
                    django_login(request, user)
                    return HttpResponse(json.dumps({'code': '200'}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'code': '100'}), content_type="application/json")
    else:
        form = AuthenticationForm()
    return render_to_response('chatting/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))


@csrf_exempt
def Team_enter(request):
    if request.method == 'POST':
        name = request.POST['teamName']
        try:
            checkName = Team.objects.get(team_name=name)
        except:
            return HttpResponse(json.dumps({'code':'100'}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({'code':'200'}),content_type="application/json")
    else:
        return render_to_response('team/enter.html',context_instance=RequestContext(request))
        
@csrf_exempt
def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('slang:login'))
    else:
        form = RegistrationForm()
    return render_to_response('chatting/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect(reverse('slang:register'))

class Team_create(TemplateView):
    template_name = "team/create.html"
    def post(self,request):
        name = request.POST['teamName']
        new_team = Team(team_name=name)
        new_team.save()
        return redirect(reverse('slang:teamEnter'));


        
class Chat(TemplateView):
    template_name = "team/chat.html"
    
class Team_selectBtn(TemplateView):
    template_name = "team/selectBtn.html"
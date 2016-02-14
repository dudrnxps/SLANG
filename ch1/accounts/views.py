from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.http import HttpResponse
from accounts.forms.authentication import AuthenticationForm
from accounts.forms.register import RegistrationForm
from django.views.decorators.csrf import csrf_exempt
 

def login(request):
    """
    Log in view
    """
    if request.method == 'POST':
        
        form = AuthenticationForm(data=request.POST)
       
        if form.is_valid():
           
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('accounts:register')
                else:
                    return redirect('/')
            else:
                return render_to_response('accounts/test1.html')
        else:
            return render_to_response('accounts/test2.html')
    else:
        form = AuthenticationForm()
    return render_to_response('accounts/login.html', {
        'form': form,
    }, context_instance=RequestContext(request))

@csrf_exempt
def register(request):
    """
    User registration view.
    """
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
        else:
            html="<h1>already ID</h1>"
            return HttpResponse(html)
    else:
        form = RegistrationForm()
    return render_to_response('accounts/register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def logout(request):
    """
    Log out view
    """
    django_logout(request)
    return redirect('accounts:register')

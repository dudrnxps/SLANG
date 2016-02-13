from django import forms
from django.contrib.auth.forms import ( UserCreationForm,AuthenticationForm )
from django.contrib.auth import authenticate, login
from chatting.models import Membership

class SignupForm(UserCreationForm):
    email = forms.EmailField(
    widget = forms.EmailInput(
        attrs = {
                'placeholder':'Email',
            }
        )
    )
    
    username = forms.CharField(
    max_length=30,
    widget = forms.TextInput(
        attrs = {
                'placeholder':'ID',
            }
        )
    )
    
    password = forms.CharField(
    widget = forms.PasswordInput(
        attrs = {
                'placeholder':'PW',
            }
        )
    )
class Meta:
    model = Membership
    fields = ("mem_username","mem_mail","mem_pass",)
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        membership = authenticate(mem_username=username, mem_pass=password)
        if not membership or not membership.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        membership = authenticate(mem_username=username, mem_pass=password)
        return membership
   
        
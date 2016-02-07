from django import forms
from django.contrib.auth.forms import UserCreationForm
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
        fields = ("username","email","password",)
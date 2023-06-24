from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3' }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3' }))
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        del self.fields['password2']
        self.fields['password1'].help_text = None

    class Meta:
        model=User
        fields= ['first_name', 'last_name', 'email', 'password1']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3' }))
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

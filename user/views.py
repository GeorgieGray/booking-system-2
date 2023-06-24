from django.shortcuts import render
from .forms import SignupForm

class Signup(FormView):
    template_name = "signup.html"
    form_class = SignupForm
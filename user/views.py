from django.shortcuts import render
from .forms import SignupForm

class Signup(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = "/booking"

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(Signup, self).form_valid(form)
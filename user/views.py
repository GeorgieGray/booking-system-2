from django.views.generic.edit import FormView
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import redirect

class Signup(FormView):
    template_name = "signup.html"
    form_class = SignupForm
    success_url = "/booking"

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        
        return super(Signup, self).form_valid(form)

class Login(FormView):
    template_name="login.html"
    form_class = LoginForm

    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            form.clean()
            user = authenticate(
                email=form.cleaned_data["username"], 
                password=form.cleaned_data["password"],
            )
            login(request, user)

            remember_me = form.cleaned_data["remember_me"]
            if not remember_me:
                request.session.set_expiry(0)

            if request.GET.__contains__('next'):
                return redirect(request.GET.__getitem__('next'))

            return redirect("/booking")
        else:            
            return redirect("login")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("home")

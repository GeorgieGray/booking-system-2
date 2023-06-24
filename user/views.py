from django.shortcuts import render
from .forms import SignupForm, LoginForm

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
                request, 
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"],
            )
            login(request, user)

            if request.GET.__contains__('next'):
                return redirect(request.GET.__getitem__('next'))

            return redirect("booking")
        else:            
            return redirect("login")

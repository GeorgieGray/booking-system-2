from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "home.html"

class Booking(TemplateView):
    template_name = "booking.html"
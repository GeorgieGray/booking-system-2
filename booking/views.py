from django.views.generic import TemplateView, CreateView
from .models import Booking
from django.contrib.admin.widgets import AdminDateWidget

class Home(TemplateView):
    template_name = "home.html"

class BookingDashboard(CreateView):
    model = Booking
    template_name = "booking.html"
    success_url = '/booking'
    fields = ['date', 'time', 'group_size', 'table']

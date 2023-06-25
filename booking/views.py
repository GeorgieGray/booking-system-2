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

    def get_form(self, form_class=None):
        form = super(BookingDashboard, self).get_form(form_class)
        form.fields['date'].widget = AdminDateWidget(attrs={'type': 'date', 'class': 'form-control mb-3' })
        form.fields['time'].widget.attrs['class'] = 'form-control'
        form.fields['group_size'].widget.attrs['class'] = 'form-control'
        form.fields['table'].widget.attrs['class'] = 'form-control'

        return form
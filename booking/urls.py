from django.urls import path
from .views import Home, Booking
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('booking/', Booking.as_view(), name="booking")
]

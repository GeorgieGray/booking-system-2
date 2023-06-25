from django.urls import path
from .views import Home, BookingDashboard
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('booking/', BookingDashboard.as_view(), name="booking")
]

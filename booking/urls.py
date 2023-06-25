from django.urls import path
from .views import Home, BookingDashboard, DeleteBooking
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('booking/', BookingDashboard.as_view(), name="booking"),
    path('booking/<pk>/delete', DeleteBooking.as_view(), name="delete_booking")
]

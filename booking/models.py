from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_time_limit = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

class Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    max_seats = models.PositiveIntegerField()
    min_seats = models.PositiveIntegerField()
    table_number = models.PositiveIntegerField()
    restaurant = models.ForeignKey(
        "Restaurant",
        on_delete=models.CASCADE
    )

class Booking(models.Model):
    BOOKING_TIMES = [
        ("01", "1am"),
        ("02", "2am"),
        ("03", "3am"),
        ("04", "4am"),
        ("05", "5am"),
        ("06", "6am"),
        ("07", "7am"),
        ("08", "8am"),
        ("09", "9am"),
        ("10", "10am"),
        ("11", "11am"),
        ("12", "12pm"),
        ("13", "1pm"),
        ("14", "2pm"),
        ("15", "3pm"),
        ("16", "4pm"),
        ("17", "5pm"),
        ("18", "6pm"),
        ("19", "7pm"),
        ("20", "8pm"),
        ("21", "9pm"),
        ("22", "10pm"),
        ("23", "11pm"),
        ("24", "12am")
    ]

    id = models.BigAutoField(primary_key=True)
    group_size = models.IntegerField()
    time = models.CharField(max_length=2, choices=BOOKING_TIMES)
    date = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    table = models.ForeignKey(
        "Table",
        on_delete=models.CASCADE
    )
    note = models.TextField(blank=True)
   
    class Meta:
        ordering = ["date", "time"]
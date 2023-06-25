from django.db import models

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
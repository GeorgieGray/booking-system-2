from django.db import models

class Restaurant(models.Model):
    id = models.BigAutoField(primary_key=True)
    table_time_limit = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=32)
    name = models.CharField(max_length=32)

from django.db import models


class Flat(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, db_index=True)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()


from django.db import models
import os
from django.conf import settings
from django.db.models import TextField
import random
import uuid

class APIToken(models.Model):
    token = models.CharField(primary_key=True, max_length=255)
    username = models.CharField(blank=True, max_length=255)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomModel(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.image_path.startswith(str(settings.MEDIA_ROOT)):
            self.image_path = os.path.relpath(self.image_path, settings.MEDIA_ROOT).replace('\\', '/')
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Locations(CustomModel):
    loc_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image_path = models.FilePathField(
        path=os.path.join(settings.MEDIA_ROOT, 'locations'),
        match=r'.*\.(jpg|png)$',
        recursive=True
    )

    def __str__(self):
        return self.name



class BGImages(CustomModel):
    image_path = models.FilePathField(
        path=os.path.join(settings.MEDIA_ROOT, 'bgimages'),
        match=r'.*\.(jpg|png)$',
        recursive=True
    )

class Hotel(CustomModel):
    hotel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    loc_id = models.ForeignKey(Locations, on_delete=models.DO_NOTHING)
    image_path = models.FilePathField(
        path=os.path.join(settings.MEDIA_ROOT, 'hotels'),
        match=r'.*\.(jpg|png)$',
        recursive=True
    )

class Room(models.Model):
    pk = models.CompositePrimaryKey("hotel_id", "room_number", "availableFrom")
    hotel_id = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    room_number = models.IntegerField()
    pricePerNight = models.IntegerField()
    roomType = models.CharField(max_length=32)
    availableFrom = models.DateField()
    availableTo = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['hotel_id', 'room_number', 'availableFrom'], name='unique_room_instance')
        ]

class Booking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    hotel_id = models.ForeignKey(Hotel, on_delete=models.DO_NOTHING)
    room_number = models.IntegerField()
    bookedFrom = models.DateField()
    bookedTo = models.DateField()
    bookedBy = models.TextField()
    bookedByEmail = models.TextField()
    paymentAmt = models.IntegerField()
    guestCount = models.IntegerField()
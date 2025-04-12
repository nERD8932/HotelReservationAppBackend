from django.contrib import admin
from .models import Locations, BGImages, Hotel, Room, APIToken, Booking

# Register your models here.
admin.site.register(Locations)
admin.site.register(BGImages)
admin.site.register(Hotel)
admin.site.register(APIToken)
admin.site.register(Booking)
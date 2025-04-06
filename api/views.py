from django.shortcuts import render
from django.http import JsonResponse
import os
import base64
from django.conf import settings
from .models import Locations, BGImages


def get_images(request):
    images = BGImages.objects.all()
    images_data = []

    image: List[BGImages]
    for image in images:
        # Read image as binary and encode in Base64
        with open(os.path.join(settings.MEDIA_ROOT, image.image_path), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        images_data.append({
            "filename": image.image_path,
            "data": encoded_string,
        })

    return JsonResponse(images_data, safe=False)

def get_locations(request):
    locations = Locations.objects.all()
    location_data = []

    locations: List[Locations]
    for location in locations:
        # Read image as binary and encode in Base64
        with open(os.path.join(settings.MEDIA_ROOT, location.image_path), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        location_data.append({
            "filename": location.name,
            "data": encoded_string,
        })

    return JsonResponse(location_data, safe=False)
    pass

def search(request):
    pass
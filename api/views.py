from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os
import base64
from django.conf import settings
from .models import Locations, BGImages, Hotel, Room
from datetime import datetime


def get_img_data(img_path):
    with open(os.path.join(settings.MEDIA_ROOT, img_path), "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

def get_images(request):
    if request.method == "GET":
        images = BGImages.objects.all()
        images_data = []

        image: List[BGImages]
        for image in images:

            images_data.append({
                "filename": image.image_path,
                "data": get_img_data(image.image_path),
            })

        return JsonResponse(images_data, safe=False)
    else:
        return HttpResponse(status=405)

def get_locations(request):
    if request.method == "GET":
        locations = Locations.objects.all()
        location_data = []

        locations: List[Locations]
        for location in locations:

            location_data.append({
                "name": location.name,
                "imageData": {
                    "filename": location.image_path,
                    "data": get_img_data(location.image_path),
                },
            })

        return JsonResponse(location_data, safe=False)
    else:
        return HttpResponse(status=405)

def search(request):
    if request.method == "GET":
        if request.GET.get("startDate", None) is not None \
                and request.GET.get("endDate", None) is not None \
                and request.GET.get("location", None) is not None:
            try:
                search_req = SearchRequestSerializer(datetime.strptime(request.GET.get("startDate"), "%Y-%m-%d"),
                                                    datetime.strptime(request.GET.get("endDate"), "%Y-%m-%d"),
                                                    request.GET.get("location"))

                return JsonResponse(search_req.fetchResults(), safe=False)
            except ValueError:
                return HttpResponse(status=405)
        else:
            return HttpResponse(status=405)
    else:
        return HttpResponse(status=405)


class SearchRequestSerializer:
    def __init__(self, start_date, end_date, location):
        self.startDate = start_date
        self.endDate = end_date
        self.location = location

    def fetchResults(self):

        if self.location == "":
            results = Room.objects.select_related('hotel_id__loc_id').filter(
                availableFom__lte=self.startDate,
                availableTo__gte=self.endDate)
        else:
            results = Room.objects.select_related('hotel_id__loc_id').filter(
                availableFom__lte=self.startDate,
                availableTo__gte=self.endDate,
                hotel_id__loc_id__name=self.location)

        image_data = {}
        response_data = []
        for room in results:
            try:
                response_data.append({
                    'hotelId': room.hotel_id,
                    'name': room.hotel_id.name,
                    'roomNumber': room.room_number,
                    'roomType': room.roomType,
                    'pricePerNight': room.pricePerNight,
                    'location': room.hotel_id.loc_id.name,
                    'imageData': {
                        'filename': room.hotel_id.image_path,
                        'data': image_data.setdefault(room.hotel_id.image_path, get_img_data(room.hotel_id.image_path)),
                    }
                })
            except Exception as e:
                print(e)
                pass
        return response_data
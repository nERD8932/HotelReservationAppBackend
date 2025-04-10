import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import os
import base64
from django.conf import settings
from .models import Locations, BGImages, Hotel, Room, APIToken
from datetime import datetime, date
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
import re

def sanitize_and_save(uploaded_file, save_path, f='JPEG'):
    with Image.open(uploaded_file) as img:
        img = img.convert('RGB')  # Strip alpha and other modes
        data = list(img.getdata())  # Force pixel processing
        clean_img = Image.new('RGB', img.size)
        clean_img.putdata(data)
        if max(clean_img.size[0], clean_img.size[1])>1600:
            clean_img.thumbnail((1600, 1600), Image.ANTIALIAS)
        clean_img.save(save_path, format=f)

def authenticate_user(request):
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return False
    token = auth.split('Bearer ')[1]
    if APIToken.objects.filter(token=token).exists():
        return True
    return False

def authenticate_admin(request):
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        return False
    token = auth.split('Bearer ')[1]
    if APIToken.objects.filter(token=token, username='admin').exists():
        return True
    return False

@csrf_exempt
def pull_from_github():
    if request.method == 'POST':
        if authenticate_admin(request):
            try:
                status = os.system(f'cd {settings.BASE_DIR} && git pull')
                return HttpResponse(f"<h1>Exited with cod: {status}</h1>", status=200)
            except Exception as e:
                return HttpResponse(f"<h1>Error: {e}</h1>", status=500)
        else:
            return HttpResponse(status=401)

@csrf_exempt
def add_hotel(request):
    if request.method == 'POST':
        if authenticate_user(request):
            hotel_name = request.POST.get('hotel_name', None)
            location = request.POST.get('location', None)
            image = request.FILES.get('image', None)
            if None in [hotel_name, location, image]:
                return HttpResponse(status=401)
            else:
                if Locations.objects.filter(name=location).exists():
                    try:
                        san_name = re.sub(r'[^a-zA-Z0-9_-]', '', hotel_name)
                        san_name = san_name.lower()
                        save_path = f'{settings.MEDIA_ROOT}/hotels/{san_name}.jpg'
                        sanitize_and_save(image, save_path)
                        Hotel.objects.create(name=hotel_name, loc_id=Locations.objects.filter(name=location)[0], image_path=save_path)
                        return HttpResponse(status=200)
                    except Exception as e:
                        return HttpResponse("Please try again later.", status=500)
                else:
                    return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)

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
        return HttpResponse(status=400)

def get_locations(request):
    if request.method == "GET":
        locations = Locations.objects.all()
        location_data = []

        locations: List[Locations]
        for location in locations:

            location_data.append({
                "locId": location.loc_id,
                "name": location.name,
                "imageData": {
                    "filename": location.image_path,
                    "data": get_img_data(location.image_path),
                },
            })

        return JsonResponse(location_data, safe=False)
    else:
        return HttpResponse(status=400)

def search(request):
    if request.method == "GET":
        if request.GET.get("startDate", None) is not None \
                and request.GET.get("endDate", None) is not None \
                and request.GET.get("location", None) is not None:
            try:
                search_req = SearchRequestSerializer(datetime.strptime(request.GET.get("startDate"), "%Y-%m-%d").date(),
                                                    datetime.strptime(request.GET.get("endDate"), "%Y-%m-%d").date(),
                                                    request.GET.get("location"))
                # print(search_req)

                # print(Room.objects.filter(availableFrom__lte=search_req.startDate))
                # print(Room.objects.filter(availableFrom__lte=date(2025, 5, 3)))

                return JsonResponse(search_req.fetchResults(), safe=False)
            except ValueError:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


class SearchRequestSerializer:
    def __init__(self, start_date, end_date, location):
        self.startDate: datetime.date = start_date
        self.endDate: datetime.date  = end_date
        self.location = location

    def __str__(self):
        return f"startDate: {str(self.startDate)} endDate: {str(self.endDate)} location: {self.location}"

    def fetchResults(self):

        if self.location == "":
            results = Room.objects.all().select_related('hotel_id', 'hotel_id__loc_id').filter(
                availableFrom__lte=self.startDate,
                availableTo__gte=self.endDate)
        else:
            results = Room.objects.all().select_related('hotel_id', 'hotel_id__loc_id').filter(
                availableFrom__lte=self.startDate,
                availableTo__gte=self.endDate,
                hotel_id__loc_id__name=self.location)

        image_data = {}
        response_data = []
        for room in results:
            try:
                response_data.append({
                    'hotelId': room.hotel_id.hotel_id,
                    'name': room.hotel_id.name,
                    'roomNumber': room.room_number,
                    'roomType': room.roomType,
                    'pricePerNight': room.pricePerNight,
                    'location': room.hotel_id.loc_id.name,
                })
                image_data.setdefault (
                    int(room.hotel_id.hotel_id),
                    {
                        "filename": room.hotel_id.image_path,
                        "data": get_img_data(room.hotel_id.image_path),
                    }
                )
            except Exception as e:
                print(e)
                pass
        return { "hotelData": response_data,  "imageData": image_data }
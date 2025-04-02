from django.shortcuts import render
from django.http import JsonResponse
import os
import base64
from django.conf import settings


def get_images(request):
    images_dir = str(os.path.join(settings.MEDIA_ROOT))
    images_data = []

    for image_name in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_name)

        # Read image as binary and encode in Base64
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

        images_data.append({
            "filename": image_name,
            "data": encoded_string,
        })

    return JsonResponse(images_data, safe=False)
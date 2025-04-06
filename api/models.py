from django.db import models
import os
from django.conf import settings

class Locations(models.Model):
    name = models.CharField(max_length=100)
    image_path = models.FilePathField(
        path=os.path.join(settings.MEDIA_ROOT, 'locations'),
        match=r'.*\.(jpg|png)$',
        recursive=True
    )

    def __str__(self):
        return self.name

class BGImages(models.Model):
    image_path = models.FilePathField(
        path=os.path.join(settings.MEDIA_ROOT, 'bgimages'),
        match=r'.*\.(jpg|png)$',
        recursive=True
    )
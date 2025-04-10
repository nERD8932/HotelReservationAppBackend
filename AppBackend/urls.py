"""
URL configuration for AppBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import  get_images, get_locations, search, pull_from_github, add_hotel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/', get_images),
    path('locations/', get_locations),
    path('search/', search),
    path('pull/', pull_from_github),
    path('add-hotel/', add_hotel),
]

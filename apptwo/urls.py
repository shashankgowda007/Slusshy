"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import Passenger_api, Rider_api, Map_api
from appthree import views as v1
from . import views

urlpatterns = [
    path("", views.rate),
    path("api", views.main2),
    path("driver", views.driver),
    path("upload", views.file),
    path("img", views.upload_image_),
    path("fetch", views.fetch),
    path("dri/<int:pk>/", Passenger_api.as_view()),
    path("pass", Rider_api.as_view()),
    path("api", Map_api.as_view()),
    # path("passenger", views.passenger),
    path("fun", v1.fun),
    path("input", views.input),
    path("signup", views.signup),
    path("login", views.login),
    path("displaydb", views.displaydb, name="db"),
    path("restfull", views.getData),
    path("R1", views.getData1),
]

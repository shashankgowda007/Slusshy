from django.contrib import admin
from django.urls import path
from . import views
from .consumers import DataConsumer
from .views import YourModelListCreateAPIView, YourModelRetrieveUpdateDestroyAPIView

# from django.conf.urls import url

urlpatterns = [
    # path("", views.fun),
    path("", views.data),
    # path("data", views.getData),
    path("view/", YourModelListCreateAPIView.as_view()),
    path("view/<int:pk>/", YourModelRetrieveUpdateDestroyAPIView.as_view()),
    # path("view", SWIFTRIDE.as_view()),
    # path("view/<str:pk>", SWIFTRIDE.as_view())
    # path("create/", views.postData1),
    # path("update/", views.update),
    # path("delete", views.delete),
    # path("delete/<str:pk>", views.delete),
]
websocket_urlpatterns = [
    path("ws/data/", DataConsumer.as_asgi()),
]

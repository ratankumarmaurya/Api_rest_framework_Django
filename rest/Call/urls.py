from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('call/',views.show),
]


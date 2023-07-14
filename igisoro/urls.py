from django.urls import path, include
from . import views

urlpatterns = [
    path("kugwiza/<igiharuro>/", views.kugwiza)
]

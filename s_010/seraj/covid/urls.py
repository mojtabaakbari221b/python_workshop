# urls.py
from django.urls import path
from .views import CovidView

urlpatterns = [
    path("", CovidView.as_view()),
]

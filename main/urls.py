from django.urls import path
from .views import get, fine

urlpatterns = [
    path('', get),
    path('fine/', fine)
]
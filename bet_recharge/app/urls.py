from django.urls import path
from .views import paage
urlpatterns = [
    path('', paage),
]

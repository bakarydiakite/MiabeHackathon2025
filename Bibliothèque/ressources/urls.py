from django.urls import path, include
from .views import progression_globale

urlpatterns = [
    path('progression/', progression_globale, name='progression_globale'),
]


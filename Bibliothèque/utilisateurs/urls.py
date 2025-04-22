from rest_framework.routers import DefaultRouter
from django.urls import path, include
from utilisateurs.views import *


route = DefaultRouter()
route.register(r'utilisateurs', UtilisateurViewSet, basename='utilisateur')

urlpatterns = [
    path('', include(route.urls)),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
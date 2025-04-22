from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


from .models import Utilisateur
from utilisateurs.serializer import UtilisateurSerializer

# CRUD utilisateurs (liste, création, update, etc.)
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    permission_classes = [permissions.IsAuthenticated]

# Connexion de l'utilisateurs personnalisé 
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({
            'token': token.key,
            'id': user.id,
            'username': user.username,
            'type': user.type,
            'statut': user.statut,
        })

# Déconnexion (supprime le token)
@api_view(['POST'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response({'message': 'Déconnexion réussie'})

# Inscription de l'utilisateur dans la base de donnée
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        User = get_user_model() 
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'Tous les champs sont requis.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Ce nom d\'utilisateur est déjà pris.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        token = Token.objects.create(user=user)
        return Response({
            'message': 'Utilisateur créé avec succès.',
            'token': token.key,
            'id': user.id,
            'username': user.username,
        }, status=status.HTTP_201_CREATED)
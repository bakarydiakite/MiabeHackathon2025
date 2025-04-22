from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from .serializers import *
from ressources.models import Ressource
from utilisateurs.serializer import UtilisateurSerializer

from rest_framework.views import APIView
class DiscussionViewSet(APIView):
    def get(self, request):
        discussions = Discussion.objects.all()
        serializer = DiscussionSerializer(discussions, many=True)
        nb_disc = len(serializers.data)
        return Response(f'{nb_disc}', serializer.data)
    def post(self, request):
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class MessageViewSet(APIView):
    def get(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
from rest_framework import serializers
from .models import Discussion, Message
from utilisateurs.serializer import UtilisateurSerializer

class DiscussionSerializer(serializers.ModelSerializer):
    createur = UtilisateurSerializer()
    class Meta:
        model = Discussion
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    auteur = UtilisateurSerializer()
    discussion = DiscussionSerializer()
    class Meta:
        model = Message
        fields = '__all__'


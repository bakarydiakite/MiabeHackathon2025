from rest_framework import serializers
from .models import Ressource, Categorie, Favori, Evaluation

class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'

# class TelechargementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Telechargement
#         fields = '__all__'
        
class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class FavoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favori
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'


from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from ressources.serializers import *
from utilisateurs.serializer import UtilisateurSerializer
from .models import Utilisateur
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = UtilisateurSerializer
    # permission_classes = [permissions.IsAuthenticated]  

# class TelechargementViewSet(viewsets.ModelViewSet):
#     queryset = Telechargement.objects.all()
#     serializer_class = TelechargementSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(utilisateur=self.request.user)

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class FavoriViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favori.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)


class EvaluationViewSet(viewsets.ModelViewSet):
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Evaluation.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def progression_globale(request):
    user = request.user
    evaluations = Evaluation.objects.filter(utilisateur=user)

    total = evaluations.count()

    print(user)
    if total == 0:
        return Response({
            "progression": 0,
            "message": "Aucune ressource évaluée pour l’instant."
        })

    progression_totale = sum(e.progression for e in evaluations)
    progression_moyenne = progression_totale / total


    return Response({
        "utilisateur": user.username,
        "total_ressources": total,
        "progression": f"{progression_moyenne} %"  # en %
    })

from django.db import models

# apprentissage/models.py
from django.db import models
from utilisateurs.models import Utilisateur
from ressources.models import Ressource

class Progression(models.Model):
    STATUT_CHOICES = [
        ('COMMENCE', 'Commencé'),
        ('EN_COURS', 'En cours'),
        ('TERMINE', 'Terminé'),
    ]
    
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='COMMENCE')
    pourcentage_completion = models.IntegerField(default=0)
    derniere_activite = models.DateTimeField(auto_now=True)
    score = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('utilisateur', 'ressource')

from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    TYPE_CHOICES = [
        ('ETUDIANT', 'Étudiant'),
        ('ENSEIGNANT', 'Enseignant'),
        ('ADMIN', 'Administrateur'),
    ]
    STATUT_CHOICES = [
        ('ACTIF', 'Actif'),
        ('INACTIF', 'Inactif'),
    ]
    
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='ETUDIANT')
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='ACTIF')
    date_inscription = models.DateTimeField(auto_now_add=True)
    dernier_acces = models.DateTimeField(auto_now=True)
    profil_image = models.ImageField(upload_to='img_profile', null=True)
    
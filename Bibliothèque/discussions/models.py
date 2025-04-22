from django.db import models

# discussions/models.py
from django.db import models
from utilisateurs.models import Utilisateur

class Discussion(models.Model):
    titre = models.CharField(max_length=200)
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    est_resolue = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

class Message(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='messages')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.auteur} dans {self.discussion.titre}"
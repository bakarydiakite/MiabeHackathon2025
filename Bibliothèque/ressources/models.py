from django.db import models

from utilisateurs.models import Utilisateur


# ressources/models.py
from django.db import models
from utilisateurs.models import Utilisateur

class Categorie(models.Model):  
    nom = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True)  
    def __str__(self):
        return self.nom

class Ressource(models.Model):
    TYPE_RESSOURCE = [
        ('LIVRE', 'Livre'),
        ('VIDEO', 'Vidéo'),
        ('EXERCICE', 'Exercice'),
    ]
    FORMAT_RESSOURCE = [
        ('PDF', 'PDF'),
        ('MP4', 'MP4'),
        ('DOCX', 'DOCX'),
    ]
    
    titre = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_RESSOURCE)
    format = models.CharField(max_length=10, choices=FORMAT_RESSOURCE)
    taille = models.IntegerField(help_text="Taille en Mo")
    fichier = models.FileField(upload_to='ressources/')  # Champ pour stocker le fichier
    date_ajout = models.DateTimeField(auto_now_add=True)
    est_public = models.BooleanField(default=True)
    createur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre

# class Telechargement(models.Model):
#     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
#     ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
#     date_telechargement = models.DateTimeField(auto_now_add=True)
#     nb_acces = models.IntegerField(default=0)

#     class Meta:
#         unique_together = ('utilisateur', 'ressource')

class Favori(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'ressource')

class Evaluation(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    progression = models.FloatField(default=0.0) 
    note = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


# class Evaluation(models.Model):
#     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
#     ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
#     note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
#     commentaire = models.TextField(blank=True)
#     date_evaluation = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('utilisateur', 'ressource')

from django.contrib import admin

from .models import Ressource, Categorie, Evaluation, Favori


admin.site.register(Ressource)
admin.site.register(Categorie)
# admin.site.register(Commentaire)
admin.site.register(Evaluation)
admin.site.register(Favori)


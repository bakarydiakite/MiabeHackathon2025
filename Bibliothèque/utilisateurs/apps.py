# utilisateurs/apps.py
from django.apps import AppConfig

class UtilisateursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'utilisateurs'  # Doit correspondre au nom du dossier de l'app
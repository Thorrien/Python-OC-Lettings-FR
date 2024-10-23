from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import logging

logger = logging.getLogger("profiles.models")


class Profile(models.Model):
    logger.info('Modèle Profile de profiles utilisé')
    """
    Modèle représentant un profil utilisateur.

    Ce modèle est utilisé pour stocker des informations supplémentaires sur un utilisateur,
    telles que sa ville préférée.

    Attributes:
        user (OneToOneField): Relation one-to-one avec le modèle User de Django. La suppression
        de l'utilisateur entraînera la suppression du profil associé.
        favorite_city (CharField): Ville préférée de l'utilisateur, champ facultatif avec une
        longueur maximale de 64 caractères.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Renvoie le nom d'utilisateur associé au profil.
        """
        return self.user.username

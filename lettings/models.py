from django.db import models

# Create your models here.
from django.core.validators import MaxValueValidator, MinLengthValidator
import logging

logger = logging.getLogger("lettings.models")


class Address(models.Model):
    logger.info('Modèle Address de lettings utilisé')
    """
    Modèle représentant une adresse.

    Attributes:
        number (PositiveIntegerField): Numéro de rue, doit être un entier positif et
        ne peut pas dépasser 9999.
        street (CharField): Nom de la rue, avec une longueur maximale de 64 caractères.
        city (CharField): Nom de la ville, avec une longueur maximale de 64 caractères.
        state (CharField): État, doit comporter exactement 2 caractères et être
        validé par un MinLengthValidator.
        zip_code (PositiveIntegerField): Code postal, doit être un entier positif
        et ne peut pas dépasser 99999.
        country_iso_code (CharField): Code ISO du pays à 3 caractères, validé par
        un MinLengthValidator.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères de l'adresse.
        Ex : "123 Main Street".
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta-information pour le modèle Address.
        verbose_name: Nom singulier pour l'affichage du modèle (ex: "Adresse").
        verbose_name_plural: Nom pluriel pour l'affichage du modèle (ex: "Adresses").
        """
        verbose_name = 'Adresse'  # Nom singulier
        verbose_name_plural = 'Adresses'  # Nom pluriel correct


class Letting(models.Model):
    logger.info('Modèle Letting de lettings utilisé')
    """
    Modèle représentant une location (Letting).

    Attributes:
        title (CharField): Titre de la location, avec une longueur maximale de 256 caractères.
        address (OneToOneField): Champ de relation one-to-one avec le modèle Address.
        La suppression de l'adresse entraînera la suppression de la location associée.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères du titre de la location.
        Ex : "Charmante maison de ville".
        """
        return self.title

"""
Modèles pour l'API Concessionnaire & Véhicules.

Concessionnaire : représente un concessionnaire avec nom et siret (non exposé dans l'API)
Véhicule : représente un véhicule lié à un concessionnaire
"""

from django.db import models


class Concessionnaire(models.Model):
    """
    Modèle Concessionnaire.
    
    Le champ 'siret' existe en base de données mais ne doit jamais être exposé
    dans l'API (ni en GET ni en POST/PUT/PATCH).
    """
    nom = models.CharField(max_length=64, verbose_name="Nom du concessionnaire")
    siret = models.CharField(
        max_length=14,
        unique=True,
        verbose_name="SIRET",
        help_text="Numéro SIRET unique (non exposé dans l'API)"
    )
    
    class Meta:
        verbose_name = "Concessionnaire"
        verbose_name_plural = "Concessionnaires"
        ordering = ['nom']
    
    def __str__(self):
        return self.nom


class Vehicule(models.Model):
    """
    Modèle Véhicule.
    
    Représente un véhicule (auto ou moto) appartenant à un concessionnaire.
    """
    TYPE_CHOICES = [
        ('auto', 'Auto'),
        ('moto', 'Moto'),
    ]
    
    type = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
        verbose_name="Type de véhicule"
    )
    marque = models.CharField(max_length=64, verbose_name="Marque")
    chevaux = models.IntegerField(verbose_name="Puissance (chevaux)")
    prix_ht = models.FloatField(verbose_name="Prix HT")
    concessionnaire = models.ForeignKey(
        Concessionnaire,
        on_delete=models.CASCADE,
        related_name='vehicules',
        verbose_name="Concessionnaire"
    )
    
    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
        ordering = ['marque', 'type']
    
    def __str__(self):
        return f"{self.marque} ({self.get_type_display()}) - {self.chevaux}ch"


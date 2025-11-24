"""
Configuration de l'interface d'administration Django.
"""

from django.contrib import admin
from .models import Concessionnaire, Vehicule


@admin.register(Concessionnaire)
class ConcessionnaireAdmin(admin.ModelAdmin):
    """Administration des concessionnaires."""
    list_display = ['id', 'nom', 'siret']
    list_filter = ['nom']
    search_fields = ['nom', 'siret']


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    """Administration des véhicules."""
    list_display = ['id', 'marque', 'type', 'chevaux', 'prix_ht', 'concessionnaire']
    list_filter = ['type', 'concessionnaire']
    search_fields = ['marque', 'concessionnaire__nom']


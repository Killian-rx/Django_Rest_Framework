"""
Serializers pour l'API Concessionnaire & Véhicules.

ConcessionnaireSerializer : expose tous les champs sauf 'siret'
VehiculeSerializer : expose tous les champs du véhicule
"""

from rest_framework import serializers
from .models import Concessionnaire, Vehicule


class ConcessionnaireSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Concessionnaire.
    
    Important : Le champ 'siret' est explicitement exclu car il ne doit
    jamais être exposé dans l'API (ni en GET ni en POST/PUT/PATCH).
    """
    
    class Meta:
        model = Concessionnaire
        fields = ['id', 'nom']
        # Le champ 'siret' est volontairement omis pour ne jamais l'exposer


class VehiculeSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Véhicule.
    
    Expose tous les champs du véhicule, y compris la relation avec le concessionnaire.
    """
    
    # Optionnel : afficher le nom du concessionnaire au lieu de juste l'ID
    concessionnaire_nom = serializers.CharField(
        source='concessionnaire.nom',
        read_only=True
    )
    
    class Meta:
        model = Vehicule
        fields = [
            'id',
            'type',
            'marque',
            'chevaux',
            'prix_ht',
            'concessionnaire',
            'concessionnaire_nom'
        ]
        read_only_fields = ['id', 'concessionnaire_nom']


class VehiculeDetailSerializer(serializers.ModelSerializer):
    """
    Serializer détaillé pour un véhicule spécifique.
    
    Utilisé pour les endpoints de détails d'un véhicule.
    """
    concessionnaire_nom = serializers.CharField(
        source='concessionnaire.nom',
        read_only=True
    )
    
    class Meta:
        model = Vehicule
        fields = [
            'id',
            'type',
            'marque',
            'chevaux',
            'prix_ht',
            'concessionnaire',
            'concessionnaire_nom'
        ]
        read_only_fields = ['id', 'concessionnaire_nom']


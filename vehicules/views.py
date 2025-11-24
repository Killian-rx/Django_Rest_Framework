"""
Views API pour l'API Concessionnaire & Véhicules.

Utilisation d'APIView (pas de ViewSet) comme demandé.
Tous les endpoints sont protégés par authentification JWT.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Concessionnaire, Vehicule
from .serializers import (
    ConcessionnaireSerializer,
    VehiculeSerializer,
    VehiculeDetailSerializer
)


class ConcessionnaireListView(APIView):
    """
    Vue pour lister tous les concessionnaires.
    
    GET /api/concessionnaires/
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Retourne la liste de tous les concessionnaires."""
        concessionnaires = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(concessionnaires, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConcessionnaireDetailView(APIView):
    """
    Vue pour obtenir les détails d'un concessionnaire.
    
    GET /api/concessionnaires/<id>/
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        """Retourne les détails d'un concessionnaire spécifique."""
        concessionnaire = get_object_or_404(Concessionnaire, pk=id)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConcessionnaireVehiculesListView(APIView):
    """
    Vue pour lister tous les véhicules d'un concessionnaire.
    
    GET /api/concessionnaires/<id>/vehicules/
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        """
        Retourne la liste de tous les véhicules d'un concessionnaire spécifique.
        """
        # Vérifier que le concessionnaire existe
        concessionnaire = get_object_or_404(Concessionnaire, pk=id)
        # Récupérer tous les véhicules de ce concessionnaire
        vehicules = Vehicule.objects.filter(concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConcessionnaireVehiculeDetailView(APIView):
    """
    Vue pour obtenir les détails d'un véhicule spécifique d'un concessionnaire.
    
    GET /api/concessionnaires/<id>/vehicules/<vehicule_id>/
    """
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id, vehicule_id):
        """
        Retourne les détails d'un véhicule spécifique d'un concessionnaire.
        Vérifie que le véhicule appartient bien au concessionnaire.
        """
        # Vérifier que le concessionnaire existe
        concessionnaire = get_object_or_404(Concessionnaire, pk=id)
        # Vérifier que le véhicule existe et appartient au concessionnaire
        vehicule = get_object_or_404(
            Vehicule,
            pk=vehicule_id,
            concessionnaire=concessionnaire
        )
        serializer = VehiculeDetailSerializer(vehicule)
        return Response(serializer.data, status=status.HTTP_200_OK)


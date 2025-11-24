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
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
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
    
    @extend_schema(
        tags=['Concessionnaires'],
        summary='Liste tous les concessionnaires',
        description='Retourne la liste complète de tous les concessionnaires enregistrés.',
        responses={
            200: ConcessionnaireSerializer(many=True),
            401: {'description': 'Non authentifié - Token JWT requis'},
        },
        examples=[
            OpenApiExample(
                'Exemple de réponse',
                value=[
                    {
                        'id': 1,
                        'nom': 'AutoPlus Paris'
                    },
                    {
                        'id': 2,
                        'nom': 'MotoCenter Lyon'
                    }
                ],
                response_only=True,
            ),
        ],
    )
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
    
    @extend_schema(
        tags=['Concessionnaires'],
        summary='Détails d\'un concessionnaire',
        description='Retourne les informations détaillées d\'un concessionnaire spécifique.',
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='ID du concessionnaire',
                required=True,
            ),
        ],
        responses={
            200: ConcessionnaireSerializer,
            401: {'description': 'Non authentifié - Token JWT requis'},
            404: {'description': 'Concessionnaire non trouvé'},
        },
        examples=[
            OpenApiExample(
                'Exemple de réponse',
                value={
                    'id': 1,
                    'nom': 'AutoPlus Paris'
                },
                response_only=True,
            ),
        ],
    )
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
    
    @extend_schema(
        tags=['Véhicules'],
        summary='Liste des véhicules d\'un concessionnaire',
        description='Retourne la liste complète de tous les véhicules appartenant à un concessionnaire spécifique.',
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='ID du concessionnaire',
                required=True,
            ),
        ],
        responses={
            200: VehiculeSerializer(many=True),
            401: {'description': 'Non authentifié - Token JWT requis'},
            404: {'description': 'Concessionnaire non trouvé'},
        },
        examples=[
            OpenApiExample(
                'Exemple de réponse',
                value=[
                    {
                        'id': 1,
                        'type': 'auto',
                        'marque': 'Peugeot',
                        'chevaux': 120,
                        'prix_ht': 25000.0,
                        'concessionnaire': 1,
                        'concessionnaire_nom': 'AutoPlus Paris'
                    },
                    {
                        'id': 2,
                        'type': 'moto',
                        'marque': 'Yamaha',
                        'chevaux': 80,
                        'prix_ht': 12000.0,
                        'concessionnaire': 1,
                        'concessionnaire_nom': 'AutoPlus Paris'
                    }
                ],
                response_only=True,
            ),
        ],
    )
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
    
    @extend_schema(
        tags=['Véhicules'],
        summary='Détails d\'un véhicule',
        description='Retourne les informations détaillées d\'un véhicule spécifique appartenant à un concessionnaire.',
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='ID du concessionnaire',
                required=True,
            ),
            OpenApiParameter(
                name='vehicule_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                description='ID du véhicule',
                required=True,
            ),
        ],
        responses={
            200: VehiculeDetailSerializer,
            401: {'description': 'Non authentifié - Token JWT requis'},
            404: {'description': 'Concessionnaire ou véhicule non trouvé'},
        },
        examples=[
            OpenApiExample(
                'Exemple de réponse',
                value={
                    'id': 1,
                    'type': 'auto',
                    'marque': 'Peugeot',
                    'chevaux': 120,
                    'prix_ht': 25000.0,
                    'concessionnaire': 1,
                    'concessionnaire_nom': 'AutoPlus Paris'
                },
                response_only=True,
            ),
        ],
    )
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


"""
URLs pour l'application vehicules.

Configuration de toutes les routes de l'API.
"""

from django.urls import path
from .views import (
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    ConcessionnaireVehiculesListView,
    ConcessionnaireVehiculeDetailView,
)

app_name = 'vehicules'

urlpatterns = [
    # Endpoints pour les concessionnaires
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:id>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    
    # Endpoints pour les véhicules d'un concessionnaire
    path(
        'concessionnaires/<int:id>/vehicules/',
        ConcessionnaireVehiculesListView.as_view(),
        name='concessionnaire-vehicules-list'
    ),
    path(
        'concessionnaires/<int:id>/vehicules/<int:vehicule_id>/',
        ConcessionnaireVehiculeDetailView.as_view(),
        name='concessionnaire-vehicule-detail'
    ),
]


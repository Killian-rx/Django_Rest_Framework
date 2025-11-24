"""
Vues pour la gestion des utilisateurs (création).

Endpoint bonus : POST /api/users/ pour créer un nouvel utilisateur.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserCreateView(APIView):
    """
    Vue pour créer un nouvel utilisateur.
    
    POST /api/users/
    Endpoint public (pas besoin d'authentification pour créer un compte).
    """
    permission_classes = [AllowAny]
    
    @extend_schema(
        tags=['Authentification'],
        summary='Créer un nouvel utilisateur',
        description='Crée un nouveau compte utilisateur. Cet endpoint est public et ne nécessite pas d\'authentification.',
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'username': {
                        'type': 'string',
                        'description': 'Nom d\'utilisateur unique',
                        'example': 'john_doe'
                    },
                    'email': {
                        'type': 'string',
                        'format': 'email',
                        'description': 'Adresse email',
                        'example': 'john@example.com'
                    },
                    'password': {
                        'type': 'string',
                        'format': 'password',
                        'description': 'Mot de passe',
                        'example': 'motdepasse123'
                    }
                },
                'required': ['username', 'email', 'password']
            }
        },
        responses={
            201: {
                'description': 'Utilisateur créé avec succès',
                'content': {
                    'application/json': {
                        'example': {
                            'message': 'Utilisateur créé avec succès.',
                            'username': 'john_doe',
                            'email': 'john@example.com'
                        }
                    }
                }
            },
            400: {
                'description': 'Erreur de validation',
                'content': {
                    'application/json': {
                        'example': {
                            'error': 'Les champs username, email et password sont requis.'
                        }
                    }
                }
            }
        },
        examples=[
            OpenApiExample(
                'Requête valide',
                value={
                    'username': 'john_doe',
                    'email': 'john@example.com',
                    'password': 'motdepasse123'
                },
                request_only=True,
            ),
            OpenApiExample(
                'Réponse succès',
                value={
                    'message': 'Utilisateur créé avec succès.',
                    'username': 'john_doe',
                    'email': 'john@example.com'
                },
                response_only=True,
            ),
        ],
    )
    def post(self, request):
        """
        Crée un nouvel utilisateur.
        
        Requiert : username, email, password
        """
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Validation des champs requis
        if not username or not email or not password:
            return Response(
                {'error': 'Les champs username, email et password sont requis.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'Un utilisateur avec ce nom existe déjà.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Créer l'utilisateur
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return Response(
                {
                    'message': 'Utilisateur créé avec succès.',
                    'username': user.username,
                    'email': user.email
                },
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {'error': f'Erreur lors de la création de l\'utilisateur: {str(e)}'},
                status=status.HTTP_400_BAD_REQUEST
            )


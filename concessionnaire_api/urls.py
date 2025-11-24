"""
URL configuration for concessionnaire_api project.

Configuration des routes principales de l'API.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from vehicules.user_views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentification JWT
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    # API endpoints
    path('api/', include('vehicules.urls')),
]


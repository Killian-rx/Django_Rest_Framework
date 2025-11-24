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
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from vehicules.user_views import UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Documentation OpenAPI (style FastAPI)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Authentification JWT
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    # API endpoints
    path('api/', include('vehicules.urls')),
]


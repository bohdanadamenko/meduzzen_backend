from api.views import UserViewSet
from Companies.views import CompanyCreateView, CompanyListView, CompanyManageView

from .views import health_check

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # Endpoint for service health check
    path('', health_check, name='health_check'),
    # Default Django admin interface
    path('admin/', admin.site.urls),
    # Endpoints for interacting with quizzes
    path('quizzes/', include('Quizzes.urls')),
    # API endpoints registered through the router
    path('api/', include(router.urls)),
    # Basic Djoser authentication endpoints
    path('auth/', include('djoser.urls')),
    # Endpoints for handling authentication tokens
    path('auth/', include('djoser.urls.authtoken')),
    # Endpoints for handling JWT tokens
    path('auth/', include('djoser.urls.jwt')),
    # Endpoints for social authentication
    path('auth/', include('social_django.urls', namespace='social')),
    # Retrieve a list of companies
    path('companies/', CompanyListView.as_view(), name='list-companies'),
    # Create a new company
    path('companies/create/', CompanyCreateView.as_view(), name='create-company'),
    # Manage a specific company (retrieve, update, delete)
    path('companies/<int:pk>/', CompanyManageView.as_view(), name='detail-company'),
]

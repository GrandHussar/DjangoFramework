from django.urls import path, include
from . import views
from .views import sample_api, get_data,SimulationReportViewSet,csrf_token_view
from rest_framework.routers import DefaultRouter


# Initialize the router
router = DefaultRouter()
router.register(r'simulation-reports', SimulationReportViewSet)

urlpatterns = [
    # Register the router URLs separately
    path('', views.index, name='index'),  # Index page
    path('welcome/', views.welcome, name='welcome'),  # Welcome page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('update_simulation/', views.update_simulation, name='update_simulation'),  # Update simulation page
    
    # API endpoints
    path('api/sample/', sample_api, name='sample-api'),  # Sample API
    path('api/data/', get_data),  # Get data API
    
    # Include the DRF router-generated URLs
    path('api/', include(router.urls)),  # All API routes from the router (for simulation-reports)
    path('csrf-token/', csrf_token_view, name='csrf-token'),
]

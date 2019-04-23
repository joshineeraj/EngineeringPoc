from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'production_areas', views.ProductionAreaViewSet)
router.register(r'feature_requests', views.FeatureRequestViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-auth-token/', obtain_jwt_token),
    path('refresh-auth-token/', refresh_jwt_token),
    path('verify-auth-token/', verify_jwt_token),
]

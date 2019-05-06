from django.urls import path
from feature_req import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('clients/', views.ClientView.as_view(), name='clients'),
    path('production_areas/', views.ProductionAreaView.as_view(), name='production_area'),
]

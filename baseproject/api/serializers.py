from feature_req.models import Client, ProductionArea, FeatureRequest
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )

"""
Serializer for Client
"""
class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'title', 'description', 'added', 'updated')

"""
Serializer for Production Area
"""
class ProductionAreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductionArea
        fields = ('id', 'title', 'description', 'added', 'updated')

"""
Serializer for FeatureRequest
"""
class FeatureRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FeatureRequest
        fields = ('id','client', 'title','description','priority', 'production_area','target_date', 'added', 'updated')


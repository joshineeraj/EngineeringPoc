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
class FeatureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureRequest
        fields = ('id','client', 'title','description','priority', 'production_area','target_date', 'added', 'updated')
    def create(self, validated_data):
        
        client_id = validated_data.get("client", None)
        priority = validated_data.get("priority", None)
        if priority is not None:
            requests_to_update = FeatureRequest.objects.filter(priority__gte=priority, client_id=client_id)
            for feature_req in requests_to_update:
                feature_req.priority = feature_req.priority + 1
            # Save all objects in 1 query
            FeatureRequest.objects.bulk_update(requests_to_update, ['priority'])
        return FeatureRequest.objects.create(**validated_data)

    
            
        
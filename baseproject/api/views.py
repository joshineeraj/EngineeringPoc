from rest_framework import viewsets
from feature_req.models import Client, ProductionArea, FeatureRequest
from api.serializers import ClientSerializer, ProductionAreaSerializer, FeatureRequestSerializer

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows clients to be viewed or edited.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductionAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Production Areas to be viewed or edited
    """
    queryset = ProductionArea.objects.all()
    serializer_class = ProductionAreaSerializer

class FeatureRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows editing and viewing feature requests
    """
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer

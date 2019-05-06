from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_jwt.compat import get_user_model

from django.urls import reverse
from feature_req import models
from api.serializers import FeatureRequestSerializer

User = get_user_model()

# Create your tests here.
class BaseTestCase(TestCase):
    def setUp(self):
        # Setting up default data for user authentication
        self.email = 'test_user@example.com'
        self.username = 'test_user'
        self.password = 'test_password'
        #Create a user
        self.user = User.objects.create_user(
            self.username, self.email, self.password)
        self.data = {
            'username': self.username,
            'password': self.password
        }
        
        #Populate sample data 
        
        #Add Clients
        self.client1 = models.Client.objects.create(title="Test Client 1", 
            description="Test Client 1 description")
        self.client2 = models.Client.objects.create(title="Test Client 2", 
            description="Test Client 2 description")
        
        #Add production areas
        self.production_area1 = models.ProductionArea.objects.create(title="Policies", 
            description="Polcies description")
        self.production_area2 = models.ProductionArea.objects.create(title="Claims", 
            description="Claims description")
        
        #Add feature requests
        models.FeatureRequest.objects.create(
            title='Test Title 1', description="Test 1 description", client=self.client1, 
            priority=1, production_area=self.production_area1, target_date = "2019-01-20")
        models.FeatureRequest.objects.create(
            title='Test Title 2', description="Test 2 description", client=self.client2, 
            priority=1, production_area=self.production_area2, target_date = "2019-01-22")
        models.FeatureRequest.objects.create(
            title='Test Title 3', description="Test 3 description", client=self.client1, 
            priority=1, production_area=self.production_area2, target_date = "2019-01-25")
        models.FeatureRequest.objects.create(
            title='Test Title 4', description="Test 4 description", client=self.client2, 
            priority=1, production_area=self.production_area1, target_date = "2019-01-26")
        
        # initialize the APIClient app
        self.client = APIClient()

    """
    Get Authentication function  
    Input: username:<allowed api user>
            password: <password>
    Returns:
    """
    def getAuthenticationToken(self):
        """ 
        Get Authentication method: 
    
        Authenticates the user via
        JWT authentication method. This function needs to be called 
        in order to allow all other APIs to be called.. 
    
        Parameters: None
        Inputs:
            url: API endpoint URL to get an authentication token  
            username (str): Username for a valid api user 
            password (str): Password for the user
            method: POST
        Returns: 
            str: Valid JWT authentication token 
    
        """

        url = reverse('get-auth')
        response = self.client.post(url, self.data)
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)


class GetAllFeatures(BaseTestCase):

    def test_get_all_feature_requests(self):
        """ 
            Get all feature requests 
        """
        #get authenticated as we are using jWT authentication method.
        self.getAuthenticationToken()
        # get API response
        response = self.client.get(reverse('feature-list'))
        # get data from db
        feature_requests = models.FeatureRequest.objects.all()
        #serialize the data
        serializer = FeatureRequestSerializer(feature_requests, many=True)
        #Compare both API data and serializer data
        self.assertEqual(response.data.get("results"), serializer.data)
        #compare the response code as 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_feature_request(self):
        """ 
            Create valid feature request
        """
        #get authenticated
        self.getAuthenticationToken()
        # get API response
        url = reverse('feature-list')
        feature_req_payload = {
            'title': 'Create Test Title 5', 
            'description': "Test 5 description", 
            'client':self.client2.id, 
            'priority':1,
            'production_area':self.production_area1.id,
            'target_date': "2019-04-27"
        }
        
        response = self.client.post(url, feature_req_payload)
        #compare the response code as 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
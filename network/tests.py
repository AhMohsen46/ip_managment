from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Subnets
from .serializers import SubnetsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_subnet(name="", network_address=""):
        if name != "" and network_address != "":
            Subnets.objects.create(name=name, network_address=network_address)

    def setUp(self):
        # add test data
        self.create_subnet("Class A", "192.0.0.0/8")
        self.create_subnet("Class B", "192.168.0.0/16")
        self.create_subnet("Class C", "192.168.1.0/24")


class GetAllSubnetsTest(BaseViewTest):

    def test_get_all_subnets(self):
        """
        This test ensures that all subnets added in the setUp method
        exist when we make a GET request to the subnets/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("subnets-all")
        )
        # fetch the data from db
        expected = Subnets.objects.all()
        serialized = SubnetsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
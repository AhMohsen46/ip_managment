from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Subnets
from .serializers import SubnetsSerializer
import json
# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_subnet(name="", network_address=""):
        if name != "" and network_address != "":
            Subnets.objects.create(name=name, network_address=network_address)

    def fetch_a_subnet(self, pk=0):
        return self.client.get(
            reverse(
                "subnets-detail",
                kwargs={
                    "pk": pk
                }
            )
        )

    def delete_a_subnet(self, pk=0):
        return self.client.delete(
            reverse(
                "subnets-detail",
                kwargs={
                    "pk": pk
                }
            )
        )


    def make_a_request(self, kind="post", **kwargs):
        """
        Make a post request to create a subnet
        :param kind: HTTP VERB
        :return:
        """
        if kind == "post":
            return self.client.post(
                reverse(
                    "subnets-list-create",
                ),
                data=json.dumps(kwargs["data"]),
                content_type='application/json'
            )

    def setUp(self):
        # add test data
        self.create_subnet("Class A", "192.0.0.0/8")
        self.create_subnet("Class B", "192.168.0.0/16")
        self.create_subnet("Class C", "192.168.1.0/24")
        self.valid_data = {
            "id": 4,
            "name": "Class C",
            "network_address": "192.168.0.0/24"
        }
        self.invalid_data = {
            "name": "Class A",
            "network_address": "192.168.0.0/8"
        }
        self.valid_id = 3
        self.invalid_id = 100



class GetAllSubnetsTest(BaseViewTest):

    def test_get_all_subnets(self):
        """
        This test ensures that all subnets added in the setUp method
        exist when we make a GET request to the subnets/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("subnets-list-create")
        )
        # fetch the data from db

        expected = Subnets.objects.all()
        serialized = SubnetsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetASingleSubentTest(BaseViewTest):

    def test_get_a_subnet(self):
        """
        This test ensures that a single subnet of a given id is
        returned
        """
        # hit the API endpoint
        response = self.fetch_a_subnet(self.valid_id)
        # fetch the data from db
        expected = Subnets.objects.get(pk=self.valid_id)
        serialized = SubnetsSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test with a subnet that does not exist
        response = self.fetch_a_subnet(self.invalid_id)
        self.assertEqual(
            response.data["message"],
            "Subnet with id: 100 does not exist"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AddSubnetsTest(BaseViewTest):

    def test_create_a_subnet(self):
        """
        This test ensures that a single subnet can be added
        """
        # hit the API endpoint
        response = self.make_a_request(
            kind="post",
            data=self.valid_data
        )
        self.assertEqual(response.data, self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # test with invalid data
        response = self.make_a_request(
            kind="post",
            data=self.invalid_data
        )
        self.assertEqual(
            response.data["message"],
            "192.168.0.0/8 has host bits set"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSubnetsTest(BaseViewTest):

    def test_delete_a_subnet(self):
        """
        This test ensures that when a subnet of given id can be deleted
        """
        # hit the API endpoint
        response = self.delete_a_subnet(1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # test with invalid data
        response = self.delete_a_subnet(100)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class ApiTestCase(APITestCase):
    def test_setting_api_return_empty(self):
        """
        Ensure that the response empty list if device_id does not exist.
        """
        url = "/api/v1/setting/?device_id=1012"

        dataResponse = []
        
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content), dataResponse)

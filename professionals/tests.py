from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from accounts.models import User
from professionals.models import Professional


class ProfessionalTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="12345678",
        )
        self.token_url = reverse("token-obtain-pair")
        response = self.client.post(
            self.token_url, {"username": "admin", "password": "12345678"}
        )
        self.access_token = response.data.get("access")
        self.professional_data = {
            "user": {"username": "test2", "password": "12345678"},
            "address": "Rua Python",
            "occupation": "Dev",
        }
        self.url = reverse("professional_create_list")

    def test_create_professional(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)
        response = self.client.post(self.url, self.professional_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_pro = Professional.objects.get(user=response.json().get("user")["id"])
        created_user = User.objects.get(id=response.json().get("user")["id"])
        self.assertEqual(created_pro.user.id, created_user.id)

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import Menu
from restaurant.api.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.pizza = Menu.objects.create(name='Pizza', price=12.99, menu_item_description='pizza')
        self.burger = Menu.objects.create(name='Burger', price=8.99, menu_item_description='burger')
        self.pasta = Menu.objects.create(name='Pasta', price=15.99, menu_item_description='pasta')

    def loginAsTestUser(self) -> None:
        self.client.login(username='testuser', password='testpassword')

    def test_view_authentication(self) -> None:
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
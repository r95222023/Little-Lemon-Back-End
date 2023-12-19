from django.urls import reverse
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json

from restaurant.models import Booking
from restaurant.api.serializers import BookingSerializer
from restaurant.api.views import MyTokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class BookingViewSetTestCase(APITestCase):
    def setUp(self) -> None:
        client = APIClient()
        # client.login(username='testuser', password='testpassword')
        # check https://stackoverflow.com/questions/2619102/djangos-self-client-login-does-not-work-in-unit-tests
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.is_active = True
        self.user.save()

        refresh = RefreshToken.for_user(self.user)

        access_token = str(refresh.access_token)
        self.auth_client = APIClient()
        self.auth_client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        # self.client.login(username='testuser', password='12345')
        self.unauth_client = APIClient()
        self.unauth_client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'abc')

        self.booking1 = Booking.objects.create(
            user= self.user,
            first_name = 'John Doe',
            number_of_guests = 2,
            reservation_date = '2023-12-12',
            reservation_slot = 11
        )
        self.booking2 = Booking.objects.create(
            user= self.user,
            first_name = 'John Doe',
            number_of_guests = 4,
            reservation_date = '2023-12-12',
            reservation_slot = 13
        )
        self.valid_payload = {
            'first_name': 'Test Booking',
            'number_of_guests': 3,
            'reservation_date': '2023-12-12',
            'reservation_slot': 13
        }
        self.invalid_payload = {
            'first_name': '',
            'number_of_guests': '',
            'reservation_date': '',
            'reservation_slot': 12
        }

    def test_create_valid_booking(self) -> None:
        response = self.auth_client.post(
            reverse('book_api'),
            data = json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invalid_booking(self) -> None:
        response = self.auth_client.post(
            reverse('book_api'),
            data = json.dumps(self.invalid_payload, cls=DjangoJSONEncoder),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_unauthorized_booking(self) -> None:
        response = self.unauth_client.post(
            reverse('book_api'),
            data = json.dumps(self.valid_payload, cls=DjangoJSONEncoder),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

from django.test import Client, TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

from restaurant.api.serializers import BookingSerializer, UserSerializer
from restaurant.models import Menu, Booking
from decimal import Decimal

class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Menu.objects.create(
            name = 'Pizza',
            price = 12.99,
            menu_item_description = 'pizza'
        )

    def test_create_menu_item(self) -> None:
        item2 = Menu.objects.create(
            name = 'Burger',
            price = 17.99,
            menu_item_description = 'burger'
        )
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(item2.name, 'Burger')
        self.assertEqual(item2.price, Decimal(17.99))
        self.assertEqual(item2.menu_item_description, 'burger')

    def test_get_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        self.assertEqual(item.name, 'Pizza')
        self.assertTrue(float(item.price) - 12.99 < 0.001)
        self.assertEqual(item.menu_item_description, 'pizza')

    def test_delete_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)


class BookingTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        booking = Booking.objects.create(
            user= self.user,
            first_name="John Doe",
            number_of_guests=4,
            reservation_date = '2023-12-12',
            reservation_slot = 11
        )
        expected_str = "John Doe for 4 guests on 2023-12-12 1100"
        self.assertEqual(str(booking), expected_str)

    def test_default_number_of_guests(self):
        booking = Booking.objects.create(
            user= self.user,
            first_name="Jane Doe",
            reservation_date = '2023-12-12',
            reservation_slot = 11
        )
        self.assertEqual(booking.number_of_guests, 1)
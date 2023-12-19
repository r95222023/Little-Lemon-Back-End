from rest_framework.serializers import ModelSerializer
from restaurant.models import Booking, Menu
from django.contrib.auth.models import User

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


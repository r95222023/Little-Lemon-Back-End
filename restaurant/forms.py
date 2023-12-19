from django.forms import ModelForm
from .models import Booking, Menu

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


# - Create/Register a user (Model Form)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# - Authenticate a user (Model Form)
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
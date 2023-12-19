# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from .models import Booking, Menu
from .forms import BookingForm, CreateUserForm, LoginForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import token_obtain_pair
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from rest_framework_simplejwt.exceptions import InvalidToken

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url="login")
@csrf_exempt
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def bookings(request):
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})

# @permission_classes([IsAuthenticated])
@csrf_exempt
def book_api(request):
    if request.method == 'POST':
        # Unauthorized user can not reserve the table.
        try:
            # invalid JWT token
            (user, token) = JWTAuthentication().authenticate(request)
        except:
            return HttpResponse('Unauthorized', status=401)

        try:
            if not user.is_authenticated:
                return HttpResponse('Unauthorized', status=401)
            data = json.load(request)
            is_slot_taken = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
                reservation_slot=data['reservation_slot']).exists()
            if not is_slot_taken:
                booking = Booking(
                    user=request.user,
                    first_name=data['first_name'],
                    number_of_guests = data['number_of_guests'],
                    reservation_date=data['reservation_date'],
                    reservation_slot=data['reservation_slot'],
                )
                booking.save()
            else:
                return HttpResponse("{'error':1}", content_type='application/json')
        except:
            # Missing data in forms
            return HttpResponseBadRequest()
    # Unauthorized user can still read the existing reservations.
    date = request.GET.get('date',datetime.today().date())

    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'registerform':form}
    return render(request, 'register.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            # print([refresh, access])
            if user is not None:
                auth.login(request, user)
                return render(request, 'loggedin.html', 
                              {'username': username, 
                               'refresh_token': refresh_token, 
                               'access_token': access_token})

    context = {'loginform':form}
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'loggedout.html')
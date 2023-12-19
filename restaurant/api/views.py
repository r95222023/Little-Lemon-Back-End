from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import BookingSerializer, UserSerializer
from restaurant.models import Booking
from django.contrib.auth.models import User


import json

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getBookings(request):
    user = request.user
    bookings = user.booking_set.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def check_user(request):
    data = json.load(request)
    username = data['username']
    is_username_used = User.objects.filter(username=username).exists()
    return Response({'user_exist': is_username_used})

# @api_view(['POST'])
# def register(request):
#     data = json.load(request)
#     username = data['username']
#     password = data['password']
#     is_username_used = User.objects.all().filter(username=username)
#     return Response({'user_exist': is_username_used})

# def register(request):
#     form = CreateUserForm()
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     context = {'registerform':form}

#     return render(request, 'crm/register.html', context=context)

# def my_login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 auth.login(request, user)
#                 return redirect("dashboard")


#     context = {'loginform':form}

#     return render(request, 'crm/my-login.html', context=context)


# def user_logout(request):

#     auth.logout(request)

#     return redirect("")



# @login_required(login_url="my-login")
# def dashboard(request):

#     return render(request, 'crm/dashboard.html')

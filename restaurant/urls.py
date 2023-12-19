from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/', views.book, name="book"),
    path('book_api/', views.book_api, name="book_api"),
    path('bookings/', views.bookings, name="bookings"),
]

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('menu/',views.menu,name='menu'),
    path('snacks/',views.snacks,name='snacks'),
    path('lunch/',views.lunch,name='lunch'),
    path('juice/',views.juice,name='juice'),
    path('desserts/',views.desserts,name='desserts'),
    path('orderpage/',views.order,name='orderpage'),
    path('contact/',views.contact,name='contact'),
]

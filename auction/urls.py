from django.urls import path
from . import views

urlpatterns = [
        path('', views.landing, name='landing'),
        path('loginpage', views.landing2, name='landing2'),
        path('donation', views.donation_form, name='donation_form'),
        path('bid/new', views.create_bid, name='create_bid')
]
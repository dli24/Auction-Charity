from django.urls import path
from . import views

urlpatterns = [
        path('', views.landing, name='landing'),
        path('loginpage/', views.landing2, name='landing2'),
        path('donation/new', views.donation_new, name='donation_new'),
        path('bid/<int:bid_id>', views.bid_detail, name='bid_detail'),
        path('bid/new', views.create_bid, name='create_bid'),
        path('endbid', views.endbid, name='endbid')
]
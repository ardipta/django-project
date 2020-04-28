from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings_index, name='listings_index'),
    path('<int:listing_id>', views.listing, name='listings'),
    path('search', views.search, name='search'),
]
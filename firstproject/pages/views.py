from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


#  pages app views

def index(request):
    latest = Listing.objects.order_by('-list_date')[:3]  # select * from listing order by list_date desc
    context = {
        'latest': latest
    }

    return render(request, 'pages/index.html', context)


def about(request):
    team = Realtor.objects.order_by('-contact_date')[:3]
    seller_of_the_month = Realtor.objects.filter(is_mvp=True).first()
    context = {
        'team': team,
        'seller_of_the_month': seller_of_the_month
    }
    return render(request, 'pages/about.html', context)

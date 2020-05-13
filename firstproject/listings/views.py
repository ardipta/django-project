from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Listing
from .model_choices import *


#  listings app views

def listings_index(request):
    listing_list = Listing.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(listing_list, 3)

    try:
        listing_list = paginator.page(page)

    except PageNotAnInteger:
        # fall back to first page
        listing_list = paginator.page(1)
    except EmptyPage:
        # fall back to last page
        listing_list = paginator.page(paginator.num_pages)

    context = {
        'listing_list': listing_list
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing_ = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing.html', {'listing': listing_})


def search(request):
    method_dict = request.GET.copy()
    keywords = method_dict.get('keywords')
    city = method_dict.get('city')
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'method_dict': method_dict,

    }

    return render(request, 'listings/search.html', context)

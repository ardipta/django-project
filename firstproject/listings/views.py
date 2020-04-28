from django.shortcuts import render


#  listings app views

def listings_index(request):
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listings.html')


def search(request):
    return render(request, 'listings/search.html')

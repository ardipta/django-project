from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    class Meta:
        model = Listing

    list_display = ['id', 'title', 'address', 'city', 'price', 'photo_main', 'realtor', 'update', 'is_published']
    list_display_links = ['id', 'title']
    list_filter = ('realtor', 'title', 'city', 'bedrooms',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'desc', 'city', 'price',)
    list_per_page = 5


admin.site.register(Listing, ListingAdmin)

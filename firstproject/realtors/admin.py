from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    class Meta:
        model = Realtor

    list_display = ['id', 'name', 'email', 'phone', 'contact_date', 'is_mvp']
    list_display_links = ['id', 'name']
    list_filter = ('name',)
    search_fields = ('name', 'photo', 'email', 'phone', 'contact_date', 'message', 'description')
    list_per_page = 5


admin.site.register(Realtor, RealtorAdmin)

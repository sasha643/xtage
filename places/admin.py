
from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'photo_reference')
    search_fields = ('name', 'address')
    list_filter = ('latitude', 'longitude')
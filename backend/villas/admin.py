from django.contrib import admin
from .models import Villa, Booking

@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price_per_night', 'is_available')
    list_filter = ('location', 'is_available')
    search_fields = ('title', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'villa', 'check_in', 'check_out', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'check_in')

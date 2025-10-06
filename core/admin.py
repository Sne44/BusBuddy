# D:\django\BusBuddy\core\admin.py

from django.contrib import admin
from .models import Bus, Route, Trip, Booking, Amenity # Import the new Amenity model

# 1. Register the Amenity model
@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)

# 2. Define the BusAdmin with the working amenities_list method
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'bus_number', 'capacity', 'amenities_list')
    search_fields = ('name', 'bus_number')
    filter_horizontal = ('amenities',) # Allows easy selection of amenities

    def amenities_list(self, obj):
        # This now works because 'amenities' is a ManyToManyField on the Bus model
        return ", ".join([a.name for a in obj.amenities.all()])
    
    amenities_list.short_description = 'Amenities' # Sets the column header name

# 3. Register other models
@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination')
    search_fields = ('origin', 'destination')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('route', 'bus', 'departure_time', 'price')
    list_filter = ('route', 'bus', 'departure_time')
    date_hierarchy = 'departure_time'

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'trip', 'seat_number', 'booking_date', 'is_paid')
    list_filter = ('is_paid', 'trip__route')
    raw_id_fields = ('user', 'trip') # Useful for quickly selecting objects
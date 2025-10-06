# core/models.py

from django.db import models
from django.conf import settings # CRITICAL: Import settings for User model reference
# from django.contrib.auth.models import User # Removed: Using settings.AUTH_USER_MODEL is safer

# Model for Bus Amenities (e.g., 'AC', 'WiFi', 'Charging Point')
class Amenity(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

# Model for the Bus Company/Type
class Bus(models.Model):
    name = models.CharField(max_length=100) # e.g., 'Volvo Sleeper'
    bus_number = models.CharField(max_length=15, unique=True)
    capacity = models.IntegerField()
    
    # --- ADDED: ManyToMany Field for Amenities ---
    amenities = models.ManyToManyField(Amenity, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.bus_number})"

# Model for a specific Route (From/To)
class Route(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.origin} to {self.destination}"

# Model for a specific Trip/Schedule
class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField() # Visible as "Bus Timings"
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2) # Visible as "Price"
    
    def __str__(self):
        return f"{self.route} on {self.departure_time.strftime('%Y-%m-%d %H:%M')}"

# Model for a User's Booking
class Booking(models.Model):
    # CORRECTED: Use settings.AUTH_USER_MODEL to link to the project's User model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Booking by {self.user.username} for {self.trip}"
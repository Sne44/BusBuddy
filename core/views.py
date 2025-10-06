# core/views.py - FINAL CONSOLIDATED & CORRECTED VERSION

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin # Required for class-based access control
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Trip, Booking # Ensure all necessary models are imported
from .forms import CustomUserCreationForm 

# ==========================================================
# 1. HOMEPAGE & TRIP LIST (Search Results)
# ==========================================================

def home(request):
    """Simple view for the homepage/landing page."""
    return render(request, 'core/index.html')

class TripListView(ListView):
    """Displays all available bus trips, ordered by departure time."""
    model = Trip
    template_name = 'core/bus_list.html'
    context_object_name = 'trips'
    # Ensures the trips are ordered chronologically by departure time
    queryset = Trip.objects.all().order_by('departure_time') 

# ==========================================================
# 2. AUTHENTICATION (Sign Up)
# ==========================================================

class SignUpView(CreateView):
    """Handles user registration using the custom form."""
    form_class = CustomUserCreationForm
    # Redirect to the login page after successful sign-up
    success_url = reverse_lazy('login') 
    template_name = 'registration/signup.html'

# ==========================================================
# 3. BOOKING FLOW (Seat Selection -> Payment -> Confirmation)
# ==========================================================

@login_required 
def book_trip(request, trip_id):
    """Handles seat selection and initiates the booking process."""
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.method == 'POST':
        # You would implement seat availability check here in a real project
        seat_number = request.POST.get('seat') or 'N/A' # Fallback for seat number
        
        # Creates the booking linked to the currently logged-in user
        booking = Booking.objects.create(
            user=request.user,
            trip=trip,
            seat_number=seat_number,
            is_paid=False # Initially unpaid
        )
        
        # Redirect to the fake payment page
        return redirect('core:fake_payment', booking_id=booking.id) 
        
    return render(request, 'core/booking_form.html', {'trip': trip})

@login_required
def fake_payment(request, booking_id):
    """Simulates a secure payment gateway and updates the booking status."""
    # Ensure the user owns the booking before proceeding
    booking = get_object_or_404(Booking, id=booking_id, user=request.user) 
    
    # If already paid, skip payment and go to confirmation
    if booking.is_paid:
        return redirect('core:booking_confirmation', booking_id=booking.id)
        
    if request.method == 'POST':
        # Simulate payment processing success
        booking.is_paid = True
        booking.save()
        
        # Redirect to a confirmation page
        return redirect('core:booking_confirmation', booking_id=booking.id) 
        
    # Pass the amount to the template for GET request
    amount = booking.trip.price
    return render(request, 'core/fake_payment.html', {'booking': booking, 'amount': amount})


@login_required
def booking_confirmation(request, booking_id):
    """Displays the final confirmation page after payment success."""
    # Ensure booking is paid and belongs to the user before showing confirmation
    booking = get_object_or_404(Booking, id=booking_id, user=request.user, is_paid=True)
    
    return render(request, 'core/confirmation.html', {'booking': booking})


# ==========================================================
# 4. USER HISTORY / DASHBOARD VIEWS 
# ==========================================================

class BookingHistoryView(LoginRequiredMixin, ListView):
    """Displays a list of all bookings made by the currently logged-in user."""
    model = Booking
    template_name = 'core/booking_history.html'
    context_object_name = 'bookings'
    
    # The essential part: filters the results to only include bookings 
    # where the user Foreign Key matches the currently logged-in user (request.user).
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_date')
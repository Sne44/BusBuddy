# core/urls.py (Corrected and Cleaned)

from django.urls import path
from . import views 

# Define the app namespace 
app_name = 'core' 

urlpatterns = [
    # ----------------------------------------------------
    # 1. PUBLIC FACING / GENERAL VIEWS
    # ----------------------------------------------------
    path('', views.home, name='home'),
    
    # Bus List / Search Results Page 
    path('buses/', views.TripListView.as_view(), name='bus_list'),

    # ----------------------------------------------------
    # 2. AUTHENTICATION VIEWS (Only custom Sign Up remains)
    # ----------------------------------------------------
    # Custom Sign Up
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    # ----------------------------------------------------
    # 3. BOOKING & PAYMENT FLOW
    # ----------------------------------------------------
    
    # Step 1: Seat selection/booking initiation
    path('book/<int:trip_id>/', views.book_trip, name='book_trip'),
    
    # Step 2: Fake Payment Gateway
    path('pay/<int:booking_id>/', views.fake_payment, name='fake_payment'),
    
    # Step 3: Confirmation Page
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    
    # ----------------------------------------------------
    # 4. USER DASHBOARD / HISTORY (NEW)
    # ----------------------------------------------------
    # Displays the user's past and pending bookings
    path('history/', views.BookingHistoryView.as_view(), name='booking_history'),
    
    # NOTE: The redundant path 'trips/<int:trip_id>/book/' has been removed.
]
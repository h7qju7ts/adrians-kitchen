from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bookings')
    else:
        form = BookingForm()
    return render(request, 'add_booking.html', {'form': form})        

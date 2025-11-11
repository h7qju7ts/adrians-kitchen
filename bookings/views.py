from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.

def home(request):
    return render(request, 'bookings/home.html')


def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your table has been booked Successfully!")
            return redirect('bookings/view_bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/add_booking.html', {'form': form}) 



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Scuccessfull")
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, 'bookings/register.html', {'form': form})    



def view_bookings(request):
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})



def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been updated Successfully ")
            return redirect('bookings/view_bookings')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/edit_booking.html', {'form': form})   



def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "You have successfully cancelled the booking")
        return redirect('bookings/view_bookings')
    return render(request, 'bookings/delete_booking.html', {'booking': booking})



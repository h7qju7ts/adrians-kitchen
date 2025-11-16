from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking

def home(request):
    return render(request, "bookings/home.html")


"""
      @login_required

      This decorator forces the user to be logged in to view the page.

      If they aren’t logged in → they are redirected to:
      /accounts/login/
      Which is the Allauth login page.
"""
@login_required
def add_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # attach logged-in user
            booking.save()
            messages.success(request, "Your table has been booked successfully!")
            return redirect("view_bookings")
    else:
        form = BookingForm()
    return render(request, "bookings/add_booking.html", {"form": form})


@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by("-date", "-time")
    return render(request, "bookings/view_bookings.html", {"bookings": bookings})


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Your booking has been updated successfully!")
            return redirect("view_bookings")
    else:
        form = BookingForm(instance=booking)
    return render(request, "bookings/edit_booking.html", {"form": form})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking has been cancelled.")
        return redirect("view_bookings")
    return render(request, "bookings/delete_booking.html", {"booking": booking})



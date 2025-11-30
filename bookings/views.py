from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from .models import Booking


def home(request):
    return render(request, "bookings/home.html")


@login_required
def add_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            # Custom message
            messages.success(request, "Your table has been booked successfully!")

            return redirect("view_bookings")
    else:
        form = BookingForm()

    return render(request, "bookings/add_booking.html", {"form": form})


@login_required
def view_bookings(request):

    # ---------------------------------------------------
    # CLEAR ALL PREVIOUS NON–BOOKING MESSAGES.
    # (login, logout, "email sent", etc.)
    # ---------------------------------------------------
    storage = messages.get_messages(request)
    storage.used = True   # instantly deletes all existing messages

    # Now load only the user's own bookings
    user_bookings = Booking.objects.filter(user=request.user)

    return render(request, "bookings/view_bookings.html", {
        "bookings": user_bookings
    })


@login_required
def edit_booking(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()

            # Custom message
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

        # Custom message
        messages.success(request, "Your booking has been cancelled.")

        return redirect("view_bookings")

    return render(request, "bookings/delete_booking.html", {"booking": booking})
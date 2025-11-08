from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add/', views.add_booking, name='add_booking'),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]

  
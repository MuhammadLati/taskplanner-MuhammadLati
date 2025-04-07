from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Room, Reservation
from datetime import datetime, timedelta
from .forms import ReservationForm
from django.db import models
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def room_list(request):
    """Display list of rooms with their current availability."""
    # Create example rooms if none exist
    if Room.objects.count() == 0:
        rooms = [
            Room.objects.create(
                name="Conference Room A",
                capacity=20,
                location="First Floor",
                is_active=True
            ),
            Room.objects.create(
                name="Meeting Room 101",
                capacity=8,
                location="Second Floor",
                is_active=True
            ),
            Room.objects.create(
                name="Study Room 1",
                capacity=4,
                location="Library",
                is_active=True
            ),
            Room.objects.create(
                name="Auditorium",
                capacity=100,
                location="Ground Floor",
                is_active=True
            )
        ]
    
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'reservations/room_list.html', {'rooms': rooms})

@login_required
def make_reservation(request, room_id):
    """Handle room reservation creation."""
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        purpose = request.POST.get('purpose')

        try:
            # Create the reservation
            reservation = Reservation.objects.create(
                room=room,
                user=request.user,
                start_time=start_time,
                end_time=end_time,
                purpose=purpose,
                status='PENDING'  # This will now work after migration
            )
            messages.success(request, 'Reservation request submitted successfully!')
            return redirect('reservations:my_reservations')
            
        except Exception as e:
            messages.error(request, f'Error creating reservation: {str(e)}')
            return render(request, 'reservations/make_reservation.html', {'room': room})

    return render(request, 'reservations/make_reservation.html', {'room': room})

@login_required
def my_reservations(request):
    """Display user's reservations."""
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    """Handle reservation cancellation."""
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    
    if reservation.start_time <= timezone.now():
        messages.error(request, 'Et voi perua mennyttä tai käynnissä olevaa varausta.')
        return redirect('reservations:my_reservations')
    
    reservation.status = 'CANCELLED'
    reservation.save()
    
    messages.success(request, f'Varaus tilaan {reservation.room.name} peruttu onnistuneesti.')
    return redirect('reservations:my_reservations')

def room_calendar(request, room_id):
    """Display calendar view for room reservations."""
    room = get_object_or_404(Room, id=room_id)
    start_date = timezone.now().date()
    end_date = start_date + timedelta(days=7)
    
    reservations = Reservation.objects.filter(
        room=room,
        start_time__date__gte=start_date,
        end_time__date__lte=end_date,
        status='APPROVED'
    ).order_by('start_time')
    
    calendar_data = []
    current_date = start_date
    while current_date <= end_date:
        day_reservations = [r for r in reservations if r.start_time.date() == current_date]
        calendar_data.append({
            'date': current_date,
            'reservations': day_reservations,
            'is_today': current_date == timezone.now().date()
        })
        current_date += timedelta(days=1)
    
    return render(request, 'reservations/room_calendar.html', {
        'room': room,
        'calendar_data': calendar_data,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('reservations:room_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

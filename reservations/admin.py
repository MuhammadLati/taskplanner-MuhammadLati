from django.contrib import admin
from .models import Room, Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'location', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'location')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'start_time', 'end_time')
    list_filter = ('room', 'user')
    search_fields = ('room__name', 'user__username')

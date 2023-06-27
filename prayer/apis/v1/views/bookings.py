from ninja import Router
from datetime import date
from django.http import HttpResponse
from ..serializers.bookings import BookingSchema, BookingCounterSchema
from prayer.services import bookings as bookings_service

router = Router()


@router.get("/counter", response=BookingCounterSchema)
def bookings_counter(request):
    return {"counter": bookings_service.bookings_counter()}


@router.get("/")
def booked_hours(request, date: date):
    return [booking_hour.strftime("%I-%M [%p]") for booking_hour in bookings_service.get_booked_datetimes(booking_date=date)]


@router.post("/")
def bookings(request, booking: BookingSchema):
    if bookings_service.save_booking(booking)[1]:
        return HttpResponse(status=201)
    else:
        return booked_hours(request, booking.datetime)

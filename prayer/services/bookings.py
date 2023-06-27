from datetime import date
from prayer.models.booking import Booking
from prayer.apis.v1.serializers.bookings import BookingSchema


def get_booked_datetimes(booking_date: date):

    """
    Function that returns all the bookings for booking_date
    :param booking_date:
    :return:
    """

    return Booking.objects.filter(
        datetime__year=booking_date.year,
        datetime__month=booking_date.month,
        datetime__day=booking_date.day,
    ).values_list('datetime', flat=True)


def save_booking(booking: BookingSchema) -> tuple:

    """
    Function that save a booking into the db
    :param booking:
    :return: (booking_db, Bool)
    """

    return Booking.objects.get_or_create(**booking.dict())


def bookings_counter() -> int:

    """
    Function that returns the number of bookings from the db
    :return: int
    """

    # Getting all booked datetimes for the day
    return Booking.objects.count()


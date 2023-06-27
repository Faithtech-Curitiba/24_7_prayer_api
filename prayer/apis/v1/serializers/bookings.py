from ninja import Schema
from datetime import datetime


class BookingSchema(Schema):
    email: str
    name: str
    phone: str
    datetime: datetime


class BookingCounterSchema(Schema):
    counter: int


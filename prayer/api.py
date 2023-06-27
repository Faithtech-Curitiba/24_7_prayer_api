from ninja import NinjaAPI

from prayer.apis.v1.views.profile import router as profile_router
from prayer.apis.v1.views.bookings import router as booking_rounter

api = NinjaAPI()

api.add_router("/profile", profile_router)
api.add_router("/bookings", booking_rounter)

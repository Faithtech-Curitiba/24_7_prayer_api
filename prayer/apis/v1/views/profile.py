from ninja import Router

from ..serializers.profile import ProfileSchema

router = Router()


@router.get("/", response=ProfileSchema)
def get_profile_me(request):
    return {"name": "John Doe", "email": "john.doe@email.com"}

import pytest

from prayer.apis.v1.serializers.profile import ProfileSchema


@pytest.mark.django_db
def test_serialize_profile(user):
    schema = ProfileSchema.from_orm(user)
    assert schema.to_dict() == {"name": user.name, "email": user.email}

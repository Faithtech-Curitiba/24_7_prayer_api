from ninja import Schema


class ProfileSchema(Schema):
    email: str
    name: str

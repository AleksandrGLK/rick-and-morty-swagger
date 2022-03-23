from marshmallow import Schema, fields, validate


class RequestPaginationMixin:
    page = fields.Integer(required=False)


class ResponsePaginationMixin:
    class PaginationSchema(Schema):
        count = fields.Int()
        pages = fields.Int()
        next = fields.Str()
        prev = fields.Str()

    info = fields.Nested(PaginationSchema)


class CharacterSchema(Schema):
    class Origin(Schema):
        name = fields.Str()
        url = fields.Str()

    class Location(Schema):
        name = fields.Str()
        url = fields.Str()

    id = fields.Int()
    name = fields.Str()
    status = fields.Str()
    species = fields.Str()
    type = fields.Str()
    gender = fields.Str()
    origin = fields.Nested(Origin)
    location = fields.Nested(Location)
    image = fields.Str()
    episode = fields.List(fields.Str())
    url = fields.Str()
    created = fields.Str()


class ListCharacterRequestSchema(RequestPaginationMixin, Schema):
    name = fields.Str(required=False)
    status = fields.Str(required=False)
    species = fields.Str(
        required=False, validate=validate.OneOf(["alive", "dead", "unknown"])
    )
    type = fields.Str(required=False)
    gender = fields.Str(
        required=False,
        validate=validate.OneOf(["female", "male", "genderless", "unknown"]),
    )


class ListCharacterResponseSchema(ResponsePaginationMixin, Schema):
    results = fields.Nested(CharacterSchema, many=True)


class EpisodeSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    air_date = fields.Str()
    episode = fields.Str()
    characters = fields.List(fields.Str())
    url = fields.Str()
    created = fields.Str()


class ListEpisodeRequestSchema(RequestPaginationMixin, Schema):
    name = fields.Str()
    episode = fields.Str()


class ListEpisodeResponseSchema(ResponsePaginationMixin, Schema):
    results = fields.Nested(EpisodeSchema, many=True)

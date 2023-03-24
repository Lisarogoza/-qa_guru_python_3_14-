from voluptuous import Schema, PREVENT_EXTRA

user = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
)
support = Schema(
    {
        "url": str,
        "text": str
    })
user_schema = Schema(
    {
        "data": user,
        "support": support
    },
    required=True,
    extra=PREVENT_EXTRA
)

users_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user],
        "support": support
    },
    required=True,
    extra=PREVENT_EXTRA,
)

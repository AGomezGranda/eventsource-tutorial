from logicblocks.event.store import EventStore
from logicblocks.event.types import NewEvent

from src.types import User

CATEGORY = "users"


def create_user(store: EventStore, user: User):
    """Creates a new user event."""
    user_id = user.id
    stream = store.stream(category=CATEGORY, stream=user_id)
    stream.publish(
        events=[
            NewEvent(
                name="user-created",
                payload={"id": user_id, "username": user.username, "email": user.email},
            )
        ]
    )
    return user_id


def update_user_email(store: EventStore, user_id: str, email: str):
    """Updates the email of a user."""
    stream = store.stream(category=CATEGORY, stream=user_id)
    stream.publish(
        events=[
            NewEvent(
                name="user-email-updated",
                payload={"id": user_id, "email": email},
            )
        ]
    )


def add_user_address(store: EventStore, user_id: str, address: str):
    """Adds a new address for a user."""
    stream = store.stream(category=CATEGORY, stream=user_id)
    stream.publish(
        events=[
            NewEvent(
                name="user-address-added",
                payload={"id": user_id, "address": address},
            )
        ]
    )

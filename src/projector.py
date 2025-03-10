from logicblocks.event.projection import Projector


def create_user_projector():
    """Creates a new user projector."""
    return Projector(
        handlers={
            "user-created": lambda state, event: {
                **state,
                "id": event.payload["id"],
                "username": event.payload["username"],
                "email": event.payload["email"],
            },
            "user-email-updated": lambda state, event: {
                **state,
                "email": event.payload["email"],
            },
            "user-address-added": lambda state, event: {
                **state,
                "address": event.payload["address"],
            },
        }
    )

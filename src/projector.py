from logicblocks.event.projection import Projector


def handle_user_created(state, event):
    return state | {
        "id": event.payload["id"],
        "username": event.payload["username"],
        "email": event.payload["email"],
    }


def handle_user_email_updated(state, event):
    return state | {
        "email": event.payload["email"],
    }


def handle_user_address_added(state, event):
    return state | {
        "address": event.payload["address"],
    }


def create_user_projector():
    """Creates a new user projector."""
    return Projector(
        handlers={
            "user-created": handle_user_created,
            "user-email-updated": handle_user_email_updated,
            "user-address-added": handle_user_address_added,
        }
    )

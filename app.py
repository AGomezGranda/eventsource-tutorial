from logicblocks.event.store import EventStore, adapters

from src.projector import create_user_projector
from src.repository import UserRepository
from test.builders.user_builder import build_user, build_user_address, build_user_id


def main():
    print("Hello from eventsource-tutorial!")

    adapter = adapters.InMemoryStorageAdapter()
    store = EventStore(adapter)

    projector = create_user_projector()
    user_repository = UserRepository(store, projector)

    # Create new user A, and update email
    user_a_id = build_user_id()
    user_a = build_user(id=user_a_id)
    new_user_a_id = user_repository.save_user(user_a)
    print(f"User saved: {new_user_a_id}")

    new_email_a = "new_email_a@example.com"
    user_repository.update_email(user_a, new_email_a)

    updated_user_a = user_repository.get(new_user_a_id)
    print(f"User updated: {updated_user_a}")

    # Create new user B, and update email and address
    user_b_id = build_user_id()
    user_b = build_user(id=user_b_id)
    new_user_b_id = user_repository.save_user(user_b)
    print(f"User saved: {new_user_b_id}")

    new_email_b = "hello_this_is_b@example.com"
    user_repository.update_email(user_b, new_email_b)

    address_b = build_user_address()
    user_repository.add_address(user_b, address_b)

    updated_user_b = user_repository.get(new_user_b_id)
    print(f"User updated: {updated_user_b}")

    # Get all users
    all_users = user_repository.get_all()
    for user in all_users:
        print(f"User: {user.username}: {user.email}")

    # Reconstruct user B
    print("Event history user B:")
    stream = store.stream(category="users", stream=user_b_id)
    for event in stream.read():
        print(f"Event: {event.id}: {event.name} - {event.occurred_at}")


if __name__ == "__main__":
    main()

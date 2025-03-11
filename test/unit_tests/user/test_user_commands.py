from logicblocks.event.store import EventStore

from src.commands import create_user, update_user_email, add_user_address
from test.builders.user_builder import build_user, build_user_address, build_user_id
from src.utils import get_event_payload

CATEGORY = "users"


class TestUserCommands:
    user_id = build_user_id()
    basic_user = build_user(
        id=user_id,
        username="John Doe",
        email="john.doe@example.com",
    )

    def test_create_user_command(self, event_store: EventStore) -> None:
        """Test create_user command function"""
        user = self.basic_user
        created_id = create_user(event_store, user)
        assert created_id == self.user_id

        stream = event_store.stream(category=CATEGORY, stream=created_id)
        events = stream.read()

        assert len(events) == 1
        assert events[0].name == "user-created"
        assert get_event_payload(events[0])["id"] == self.user_id
        assert get_event_payload(events[0])["username"] == "John Doe"
        assert get_event_payload(events[0])["email"] == "john.doe@example.com"

    def test_update_user_email_command(self, event_store: EventStore) -> None:
        """Test update_user_email function"""
        user = self.basic_user
        create_user(event_store, user)
        email = "john.doe123@example.com"
        update_user_email(store=event_store, user_id=self.user_id, email=email)

        stream = event_store.stream(category=CATEGORY, stream=self.user_id)
        events = stream.read()

        assert len(events) == 2
        assert events[1].name == "user-email-updated"
        assert get_event_payload(events[1])["id"] == self.user_id
        assert get_event_payload(events[1])["email"] == email

    def test_add_user_address_command(self, event_store: EventStore) -> None:
        """Test add_user_address function"""
        user = self.basic_user
        create_user(event_store, user)
        address = build_user_address()
        add_user_address(store=event_store, user_id=self.user_id, address=address)

        stream = event_store.stream(category=CATEGORY, stream=self.user_id)
        events = stream.read()

        assert len(events) == 2
        assert events[1].name == "user-address-added"
        assert get_event_payload(events[1])["id"] == self.user_id
        assert get_event_payload(events[1])["address"] == address

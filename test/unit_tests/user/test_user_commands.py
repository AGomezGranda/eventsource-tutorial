import uuid
from logicblocks.event.store import EventStore

from src.commands import create_user, update_user_email, add_user_address
from test.builders.user_builder import build_user
from src.utils import get_event_payload

CATEGORY = "users"


class TestUserCommands:
    user_id = str(uuid.uuid4())
    basic_user = build_user(
        id=user_id,
        username="John Doe",
        email="john.doe@example.com",
    )

    def test_create_user_command(self, event_store: EventStore) -> None:
        """Test create_user command function"""
        user = self.basic_user
        created_id, stream = create_user(event_store, user)
        assert created_id == self.user_id

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
        stream = update_user_email(store=event_store, user_id=self.user_id, email=email)
        events = stream.read()

        assert len(events) == 2
        assert events[1].name == "user-email-updated"
        assert get_event_payload(events[1])["id"] == self.user_id
        assert get_event_payload(events[1])["email"] == email

    def test_add_user_address_command(self, event_store: EventStore) -> None:
        """Test add_user_address function"""
        user = self.basic_user
        create_user(event_store, user)
        address = "123 Main St"
        stream = add_user_address(
            store=event_store, user_id=self.user_id, address=address
        )
        events = stream.read()

        assert len(events) == 2
        assert events[1].name == "user-address-added"
        assert get_event_payload(events[1])["id"] == self.user_id
        assert get_event_payload(events[1])["address"] == address

from logicblocks.event import store
from src.commands import add_user_address, create_user, update_user_email
from test.builders.user_builder import build_user, build_user_id

from logicblocks.event.projection import Projector

CATEGORY = "users"


class TestUserProjector:
    user_id = build_user_id()
    user_a = build_user(id=user_id)

    def test_user_projector_user_created(
        self, user_projector: Projector, event_store: store.EventStore
    ) -> None:
        """Test projection of user created event"""
        created_id = create_user(event_store, user=self.user_a)
        stream = event_store.stream(category=CATEGORY, stream=created_id)
        projection = user_projector.project({}, stream.read())

        assert projection.state["id"] == self.user_a.id
        assert projection.state["email"] == self.user_a.email
        assert projection.state["username"] == self.user_a.username

    def test_user_projector_multiple_events(
        self, user_projector: Projector, event_store: store.EventStore
    ) -> None:
        """Test projection of multiple user events"""

        create_user(event_store, user=self.user_a)
        update_user_email(event_store, user_id=self.user_a.id, email="test@example.com")
        add_user_address(event_store, user_id=self.user_a.id, address="123 Main St")

        stream = event_store.stream(category=CATEGORY, stream=self.user_a.id)
        projection = user_projector.project({}, stream.read())

        assert projection.state["id"] == self.user_a.id
        assert projection.state["email"] == "test@example.com"
        assert projection.state["username"] == self.user_a.username
        assert projection.state["address"] == "123 Main St"

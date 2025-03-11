from logicblocks.event.projection import Projector
from logicblocks.event.store import EventStore

from src.repository import UserRepository
from test.builders.user_builder import build_user, build_user_address, build_user_id
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

CATEGORY = "users"


class TestIntegration:
    def test_user_lifecycle(
        self, event_store: EventStore, user_projector: Projector
    ) -> None:
        """Test the complete lifecycle of a user through the system"""
        repository = UserRepository(store=event_store, projector=user_projector)

        user_id = build_user_id()
        user = build_user(id=user_id)

        repository.save_user(user)

        user_repo = repository.get(user_id=user_id)
        assert user_repo is not None

        new_email = "new_email@example.com"
        repository.update_email(user=user, new_email=new_email)

        address = build_user_address()
        repository.add_address(user=user, address=address)

        updated_user = repository.get(user_id=user_id)
        assert updated_user is not None
        assert updated_user.id == user_id
        assert updated_user.username == user.username
        assert updated_user.email == new_email
        assert updated_user.address == address

        stream = event_store.stream(category=CATEGORY, stream=user_id)
        events = stream.read()

        assert len(events) == 3
        assert events[0].name == "user-created"
        assert events[1].name == "user-email-updated"
        assert events[2].name == "user-address-added"

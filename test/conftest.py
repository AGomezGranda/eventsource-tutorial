import pytest
from logicblocks.event.store import EventStore, adapters

from logicblocks.event.projection import Projector

from src.projector import create_user_projector


@pytest.fixture
def event_store() -> EventStore:
    """Create an in-memory event store."""
    adapter = adapters.InMemoryStorageAdapter()
    return EventStore(adapter)


@pytest.fixture
def user_projector() -> Projector:
    """Create a user projector"""
    return create_user_projector()


# @pytest.fixture
# def user_repository(event_store: EventStore, user_projector: Projector) -> UserRepository:
#     """Create a user repository"""
#     return UserRepository(event_store, user_projector)

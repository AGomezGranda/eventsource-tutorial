from faker import Faker
from typing_extensions import Any, Dict, Optional
from logicblocks.event.types import NewEvent

fake = Faker()


def build_event(
    name: Optional[str] = None,
    payload: Optional[Dict[str, Any]] = None,
) -> NewEvent:
    """Builds a NewEvent object for testing."""
    return NewEvent(name=(name or fake.name()), payload=(payload or {}))

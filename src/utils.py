from typing import Any, Dict
from logicblocks.event.types.event import StoredEvent


def get_event_payload(event: StoredEvent) -> Dict[str, Any]:
    """Returns the payload of the stored event."""
    return dict(event.payload)

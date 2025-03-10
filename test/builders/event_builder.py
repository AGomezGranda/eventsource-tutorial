import datetime
from logicblocks.event.utils import Clock
from logicblocks.event.utils.clock import SystemClock
from typing_extensions import Any, Dict, Optional
from logicblocks.event.types import NewEvent

class NewEventBuilder:
    """Builder for Event objects."""

    def __init__(self) -> None:
            self._name: str = "test-event"
            self._payload: Dict[str, Any] = {}
            self._observed_at = Optional[datetime.datetime.now()]
            self._ocurred_at = Optional[datetime.datetime.now()]

    def with_name(self, name: str) -> 'NewEventBuilder':
        self._name = name
        return self

    def with_payload(self, payload: Dict[str, Any]) -> 'NewEventBuilder':
        self._payload = payload
        return self

    def with_observed_at(self, observed_at: datetime.datetime) -> 'NewEventBuilder':
        self._observed_at = observed_at
        return self

    def with_occurred_at(self, occurred_at: datetime.datetime) -> 'NewEventBuilder':
        self._ocurred_at = occurred_at
        return self

    def build(self) -> NewEvent:
        """Builds a NewEvent object for testing."""
        return NewEvent(
            name=self._name,
            payload=self._payload,
       )

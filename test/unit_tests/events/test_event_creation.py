from test.builders.event_builder import build_event


class TestEventCreation:
    def test_create_event(self) -> None:
        """Test creating an event."""
        event = build_event(name="test_event", payload={"key": "value"})

        assert event.name == "test_event"
        assert event.payload == {"key": "value"}
        assert event.observed_at is not None
        assert event.occurred_at is not None

from datetime import datetime, timezone
from uuid import uuid4
from typing import Optional

from types import User

class UserBuilder:
    """Class for creating User objects for testing"""
    def __init__(self) -> None:
        self._id: str = str(uuid4())
        self._username: str = 'testuser'
        self._email: str = 'test@example.com'
        self._address: Optional[str] = None
        self._phone: Optional[str] = None
        self._created_at: datetime = datetime.now(timezone.utc)
        self._updated_at: Optional[datetime] = None

    def with_id(self, id: str) -> 'UserBuilder':
        self._id = id
        return self

    def with_username(self, username: str) -> 'UserBuilder':
        self._username = username
        return self

    def with_email(self, email: str) -> 'UserBuilder':
        self._email = email
        return self

    def with_address(self, address: str) -> 'UserBuilder':
        self._address = address
        return self

    def with_phone(self, phone: str) -> 'UserBuilder':
        self._phone = phone
        return self

    def with_created_at(self, created_at: datetime) -> 'UserBuilder':
        self._created_at = created_at
        return self

    def with_updated_at(self, updated_at: datetime) -> 'UserBuilder':
        self._updated_at = updated_at
        return self

    def build(self) -> User:
        """Builds a User object for testing."""
        return User(
            id=self._id,
            username=self._username,
            email=self._email,
            created_at=self._created_at,
            updated_at=self._updated_at,
            address=self._address,
            phone=self._phone
        )

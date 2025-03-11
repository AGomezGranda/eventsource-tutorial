from typing import Optional
from faker import Faker
from src.model import User

fake = Faker()


def build_user_id() -> str:
    return str(fake.uuid4())


def build_user_address() -> str:
    return fake.address()


def build_user(
    id: Optional[str] = None,
    username: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
) -> User:
    return User(
        id=(id or build_user_id()),
        username=(username or fake.name()),
        email=(email or fake.email()),
        address=(address or None),
    )

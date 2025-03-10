from typing import Optional
from faker import Faker
from src.types import User

fake = Faker()


def build_user(
    id: Optional[str] = None,
    username: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
) -> User:
    return User(
        id=(id or str(fake.uuid4())),
        username=(username or fake.name()),
        email=(email or fake.email()),
        address=(address or fake.address()),
    )

from typing import List, Optional
from logicblocks.event.projection import Projector
from logicblocks.event.store import EventStore

from src.model import User

from src.commands import add_user_address, create_user, update_user_email


class UserRepository:
    def __init__(self, store: EventStore, projector: Projector):
        self.store = store
        self.projector = projector

    def save_user(self, user: User):
        return create_user(self.store, user)

    def update_email(self, user: User, new_email: str):
        update_user_email(self.store, user_id=user.id, email=new_email)

    def add_address(self, user: User, address: str):
        add_user_address(self.store, user_id=user.id, address=address)

    def get(self, user_id: str) -> Optional[User]:
        stream = self.store.stream(category="users", stream=user_id)
        events = stream.read()
        if not events:
            return None
        user_dict = self.projector.project({}, events)
        return User.deserialise(user_dict.state)

    def get_all(self) -> List[User]:
        category = self.store.category(category="users")
        streams = category.read()

        users = []
        for stream in streams:
            user = self.get(stream.payload["id"])
            if user:
                users.append(user)
        return users

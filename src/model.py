from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel


class User(BaseModel):
    """User class"""

    id: str
    username: str
    email: str
    address: Optional[str] = None
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def serialise(self) -> Dict[str, any]:
        return self.model_dump()

    @classmethod
    def deserialise(cls, data: Dict[str, any]) -> "User":
        return User(**data)

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    """User class"""

    id: str
    username: str
    email: str
    address: Optional[str]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

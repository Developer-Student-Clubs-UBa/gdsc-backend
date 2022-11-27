from typing import Optional

from pydantic import BaseModel

#
# class Item(BaseModel):
#     task: str


class User(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]
    username: Optional[str]
    avatar_link: Optional[str]
    bio: Optional[str]

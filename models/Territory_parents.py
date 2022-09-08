from typing import Optional
from sqlmodel import Field, SQLModel


class Territory_parents(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    child_id: str = Field(index=True)
    parent_id: str
    created_at: str

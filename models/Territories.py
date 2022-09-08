from typing import Optional
from sqlmodel import Field, SQLModel


class Territories(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    kind: str
    created_at: str
    updated_at: str
    is_current: str
    population: str
    official_website_url: str
    articles_count: str
    admin_docs_count: str
    impacters_count: str
    websites_count: str
    sources_count: str

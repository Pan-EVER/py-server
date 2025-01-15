from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    data: list[T]
    page: int
    page_size: int
    total: int
    has_next: bool

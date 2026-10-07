from pydantic import BaseModel


class UserResponseDto(BaseModel):
    id: int
    name: str
    email: str
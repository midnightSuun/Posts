from typing import Annotated, List

from fastapi import Depends
from app.users.dto.user_response_dto import UserResponseDto
from app.users.users_repository import UsersRepository


class UserService:
    def __init__(self, users_repository: Annotated[UsersRepository, Depends()]):
        self.users_repository = users_repository

    async def get_users(self)->List[UserResponseDto]:
        users = await self.users_repository.get_users()
        
        return [
            UserResponseDto(id=user.id, name=user.name, email=user.email) 
            for user in users
        ]

    async def get_user(self, user_id: int) -> UserResponseDto | None:
        user = await self.users_repository.get_user(user_id)

        if user is None:
            return None

        return UserResponseDto(id=user.id, name=user.name, email=user.email)
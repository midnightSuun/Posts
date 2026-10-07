from typing import List
from app.users.dto.user_response_dto import UserResponseDto


class UserService:
    def get_users(self)->List[UserResponseDto]:
        return [
            UserResponseDto(id=1, name="John Doe", email="john.doe@example.com"), 
            UserResponseDto(id=2, name="Jane Doe", email="jane.doe@example.com"),
            UserResponseDto(id=3, name="Jim Doe", email="jim.doe@example.com"),
        ]
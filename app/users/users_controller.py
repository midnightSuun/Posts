from typing import List
from fastapi import APIRouter

from app.users.dto.user_response_dto import UserResponseDto
from app.users.service import UserService


router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService()

@router.get("/")
def get_users()->List[UserResponseDto]:
    return user_service.get_users()
from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException

from app.users.dto.user_response_dto import UserResponseDto
from app.users.users_service import UserService


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def get_users(users_service: Annotated[UserService, Depends()]) -> List[UserResponseDto]:
    return await users_service.get_users()

@router.get("/{user_id}")
async def get_user(
    user_id: int, 
    users_service: Annotated[UserService, Depends()]
) -> UserResponseDto:
    user = await users_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
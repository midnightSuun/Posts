from typing import List

from sqlalchemy import select
from app.db import DbSession
from app.models import User


class UsersRepository:
    def __init__(self, db: DbSession):
        self.db = db

    async def get_users(self) -> List[User]:
        result = await self.db.execute(select(User))
        return list(result.scalars().all())

    async def get_user(self, user_id: int) -> User | None:
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
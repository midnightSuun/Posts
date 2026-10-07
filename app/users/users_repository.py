from typing import List

from sqlalchemy import select
from app.db import DbSession
from app.models import Users


class UsersRepository:
    def __init__(self, db: DbSession):
        self.db = db

    async def get_users(self) -> List[Users]:
        result = await self.db.execute(select(Users))
        return list(result.scalars().all())

    async def get_user(self, user_id: int) -> Users | None:
        result = await self.db.execute(select(Users).where(Users.id == user_id))
        return result.scalar_one_or_none()
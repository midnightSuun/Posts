import datetime

from sqlalchemy import DateTime, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Text, UniqueConstraint, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class SchemaMigrations(Base):
    __tablename__ = 'schema_migrations'
    __table_args__ = (
        PrimaryKeyConstraint('version', name='schema_migrations_pkey'),
    )

    version: Mapped[str] = mapped_column(String, primary_key=True)


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pkey'),
        UniqueConstraint('email', name='user_email_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)

    post: Mapped[list['Post']] = relationship('Post', back_populates='author')


class Post(Base):
    __tablename__ = 'post'
    __table_args__ = (
        ForeignKeyConstraint(['author_id'], ['user.id'], name='post_author_id_fkey'),
        PrimaryKeyConstraint('id', name='post_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=text('now()'))
    author_id: Mapped[int] = mapped_column(Integer, nullable=False)

    author: Mapped['User'] = relationship('User', back_populates='post')

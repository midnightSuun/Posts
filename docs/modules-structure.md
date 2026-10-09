# Module structure

Each domain lives in its own folder under `app/<module>/`. The reference implementation is `app/users/`.

```
app/users/
├── __init__.py                 # public API of the module: exports router
├── users_controller.py         # HTTP: routes, status codes
├── users_service.py            # business logic and mapping to DTOs
├── users_repository.py         # database access
└── dto/
    └── user_response_dto.py    # API response contract
```

Table models live in `app/models.py`. The database session lives in `app/db.py` (`DbSession`).

The router is registered in `app/main.py`:

```python
from app.users import router as users_router

app.include_router(users_router)
```

## Layers

A request flows top to bottom: **controller → service → repository**. Each layer talks only to the layer directly below it.

| Layer | File | Responsibility |
| --- | --- | --- |
| Controller | `<module>_controller.py` | `APIRouter`, path, query and path parameters, HTTP errors. Returns a DTO. |
| Service | `<module>_service.py` | Module use cases. Maps ORM models to DTOs. |
| Repository | `<module>_repository.py` | SQLAlchemy queries. Returns models from `app/models.py`. |
| DTO | `dto/<entity>_<purpose>_dto.py` | Pydantic schemas for the public contract. |

FastAPI wires dependencies with `Depends()`:

- the controller receives the service;
- the service receives the repository;
- the repository receives `DbSession`.

```python
# controller
users_service: Annotated[UserService, Depends()]

# service
users_repository: Annotated[UsersRepository, Depends()]

# repository
db: DbSession
```

## Naming

- The module folder is the plural domain name: `users`.
- Layer files: `<module>_controller.py`, `<module>_service.py`, `<module>_repository.py`.
- Router: `prefix="/<module>"`, `tags=["<module>"]`.
- `__init__.py` exports `router` only.
- DTO: class `UserResponseDto`, file `user_response_dto.py`.
- The service is named after the entity (`UserService`). The repository is named after the module (`UsersRepository`).

## What each layer does

The **controller** calls the service and turns a missing entity into an HTTP response.

```python
user = await users_service.get_user(user_id)
if user is None:
    raise HTTPException(status_code=404, detail="User not found")
return user
```

The **service** reads data from the repository and maps model fields into a DTO.

```python
return UserResponseDto(id=user.id, name=user.name, email=user.email)
```

The **repository** runs the query and returns `User` or `None`.

```python
result = await self.db.execute(select(User).where(User.id == user_id))
return result.scalar_one_or_none()
```

## New module

1. Create `app/<module>/` with `__init__.py`, a controller, a service, a repository, and `dto/`.
2. Define the endpoints in the controller and export `router` from `__init__.py`.
3. Register the router in `app/main.py`.
4. Add tables through a migration and regenerate `app/models.py`. Keep model declarations out of the module.

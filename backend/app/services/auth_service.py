from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories import user_repository
from app.schemas.auth import SignupRequest

password_hasher = PasswordHash.recommended()


class EmailAlreadyRegistered(Exception):
    pass


def signup(db: Session, data: SignupRequest) -> User:
    email = str(data.email).lower()

    existing_user = user_repository.get_by_email(db, email)
    if existing_user:
        raise EmailAlreadyRegistered

    password_hash = password_hasher.hash(data.password)

    return user_repository.create_user(
        db=db,
        name=data.name,
        email=email,
        password_hash=password_hash,
    )

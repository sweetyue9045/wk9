from fastapi import HTTPException, status
from router.schemas import UserRequestSchema
from sqlalchemy.orm.session import Session
from .user_feed import user

from db.models import DbUser

def db_feed(db: Session):
    new_user_list = [DbUser(
        username=user["username"],
        email=user["email"],
    ) for user in user]
    db.query(DbUser).delete()
    db.commit()
    db.add_all(new_user_list)
    db.commit()
    return db.query(DbUser).all()

def create(db: Session, request: UserRequestSchema) -> DbUser:
    new_user = DbUser(
        username=request.username,
        email=request.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session) -> list[DbUser]:
    users = db.query(DbUser).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Users not found')
    return users

def get_user_by_id(user_id: int, db: Session) -> DbUser:
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id = {id} not found')
    return user
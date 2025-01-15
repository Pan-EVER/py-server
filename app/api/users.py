from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import User as UserSchema, UserCreate, UserUpdate
from app.models.user import User as UserModel
from app.schemas.pagination import PaginatedResponse
from app.services.user import (
    get_user,
    get_users,
    get_user_by_email,
    create_user,
    update_user,
    delete_user,
)
from app.core.database import get_db

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserSchema)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user=user)


@router.get("/", response_model=PaginatedResponse[UserSchema])
def read_users(page: int = 1, page_size: int = 20, db: Session = Depends(get_db)):
    skip = (page - 1) * page_size
    limit = page_size
    users = get_users(db, skip=skip, limit=limit)
    total = db.query(UserModel).count()
    return {
        "data": users,
        "page": page,
        "page_size": page_size,
        "total": total,
        "has_next": skip + limit < total,
    }


@router.get("/{user_id}", response_model=UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=UserSchema)
def update_existing_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # 只更新传入的字段
    update_data = user.model_dump(exclude_unset=True)
    return update_user(db, user_id=user_id, user=update_data)


@router.delete("/{user_id}", response_model=UserSchema)
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return delete_user(db, user_id=user_id)

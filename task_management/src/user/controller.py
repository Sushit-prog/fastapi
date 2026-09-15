from fastapi import HTTPException
from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from src.user.models import UserModel
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()

def get_password_hash(password):
  return password_hash.hash(password)

def register(body:UserSchema, db:Session):
  
  # checks: username validation, email validation
  is_user = db.query(UserModel).filter(UserModel.username==body.username).first()
  if is_user:
    raise HTTPException(400, detail="Username already exists")
  
  is_user = db.query(UserModel).filter(UserModel.email==body.email).first()
  if is_user:
    raise HTTPException(400, detail="email already exists")

  # if user does not exists after validation checks then we need to create new user
  hash_password = get_password_hash(body.password)
  
  new_user = UserModel(
    name = body.name,
    username=body.username,
    hash_password = hash_password,
    email = body.email
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user


def login_user()
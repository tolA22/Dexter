

from sqlalchemy.orm import Session 
from model import User
from schema import CreateUserRequest

def create_user(data:CreateUserRequest, db:Session):
    """ 
    Creates user
    """
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user



def get_users(db:Session):
    """ 
    Returns all users
    """
    return db.query(User).all()

from sqlalchemy.orm import Session 
from schema import SendGroupMessageRequest
from model import ChatMessage

def send_group_message(data:SendGroupMessageRequest, db:Session):
    
    message = ChatMessage(**data.dict())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def view_all_messages(db:Session):
    return db.query(ChatMessage).all()

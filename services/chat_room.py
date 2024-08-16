from sqlalchemy.orm import Session 
from model import ChatRoom , User, UserChatRoom

from schema import CreateChatRoomRequest,AddUserToChatRoomRequest

from typing import Any 

def create_chatroom(data:CreateChatRoomRequest, db:Session):

    #TODO: raise proper HTTP Exception 
    chat_room = ChatRoom(**data.dict())
    db.add(chat_room)
    db.commit()
    db.refresh(chat_room)
    return chat_room


def add_users_to_chatroom(data:AddUserToChatRoomRequest, db:Session):
    #get user ids
    user_ids = data.user_ids.split(",")
    
    for user_id in user_ids:
        user_chat_room = UserChatRoom(user_id=int(user_id), chat_room_id=data.chat_room_id )
        db.add(user_chat_room)
        db.commit()

    return {}

def view_all_user_chat_rooms(db:Session):
    return db.query(UserChatRoom).all()


def view_all_chat_rooms(db:Session):
    return db.query(ChatRoom).all()

def view_user_chat_rooms(user_id:int, db:Session):
    return {} 


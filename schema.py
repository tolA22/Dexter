from typing import Optional, Any
from pydantic import BaseModel
from datetime import datetime
from model import CHAT_TYPE


class MyRequest(BaseModel):
    first_name:str 

class DateModel(BaseModel):
    created_at: datetime 
    updated_at:datetime 
    deleted_at:datetime 

class CreateUserRequest(BaseModel):
    first_name:str 
    last_name:str 
    email:str 


    
class CreateChatRoomRequest(BaseModel):
    user_id:int 
    name:str 
    chat_type: CHAT_TYPE = CHAT_TYPE.GROUP

class User(CreateUserRequest):
    id:int 
    chat_rooms: Any 

    class Config:
        orm_mode=True 

class AddUserToChatRoomRequest(BaseModel):
    chat_room_id:int 
    user_ids:str #comma separated str 


class SendGroupMessageRequest(BaseModel):
    user_chat_room_id:int 
    text:str 
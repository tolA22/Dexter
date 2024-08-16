

from sqlalchemy import Column, Integer, String,DateTime, Enum, Text,ForeignKey
from sqlalchemy.orm import (
    declarative_base,
    relationship
)
import enum 
# from sqlalchemy.ext.declarative import as_declarative

import helper as dexter_helper 


class EmptyTimestampBase:
    __abstract__ = True
    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    created_at = Column(DateTime, default=dexter_helper.current_utc_time)
    updated_at = Column(
        DateTime,
        default=dexter_helper.current_utc_time,
        onupdate=dexter_helper.current_utc_time,
    )
    deleted_at = Column(DateTime,nullable=True)


EmptyTimestampBase = declarative_base(cls=EmptyTimestampBase)

class CHAT_TYPE(str, enum.Enum):
    SINGLE = "SINGLE" #single chat between two users
    GROUP = "GROUP" #a group chat between multiple users


class User(EmptyTimestampBase):

    __tablename__ = "user"
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, index=True)

    #relationship with chatroom  -- a user can create multiple chat_rooms
    chat_rooms = relationship("ChatRoom",back_populates="user")

    #other patient info can be added
    ...



class ChatRoom(EmptyTimestampBase):
    __tablename__ = "chat_room"
    name = Column(String,index=True) #
    chat_type = Column(Enum(CHAT_TYPE), nullable=False) # Can be single or group


    #relationship with user  -- a user can create multiple chat_rooms
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="chat_rooms")

    

class UserChatRoom(EmptyTimestampBase):
    #manages relationship between user and chatroom
    __tablename__ = "user_chat_room"
    
    #relationship with chat_room; a chatroom can appear multiple times under different users
    chat_room_id = Column(Integer, ForeignKey("chat_room.id"),index=True)
    # chatroom = relationship("ChatRoom", foreign_keys="chat_room.id")

    #relationship with user; a user can appear multiple times under different chatrooms
    user_id = Column(Integer, ForeignKey("user.id"),index=True)
    # user = relationship("ChatRoom", foreign_keys="user.id")

    #relationship with chatmessages
    chat_messages = relationship("ChatMessage",back_populates="user_chat_room")

class ChatMessage(EmptyTimestampBase):
    __tablename__ = "chat_message"
    #keeping it simple, we will be storing just text for now
    text= Column(Text, nullable=False, index=True)
    
    #relationship with user

    user_chat_room_id = Column(Integer, ForeignKey("user_chat_room.id"),index=True)
    user_chat_room = relationship("UserChatRoom", back_populates="chat_messages")


    
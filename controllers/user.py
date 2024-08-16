from fastapi import APIRouter, Depends, HTTPException, Request, status

from schema import CreateUserRequest, CreateChatRoomRequest, AddUserToChatRoomRequest, SendGroupMessageRequest
from database import get_db
from services import user as user_service 
from services import chat_room as chat_room_service 
from services import chat_message as chat_message_service 

router = APIRouter()


@router.post("/user")
def create_user(
    data: CreateUserRequest,
    db=Depends(get_db),
):
    return user_service.create_user(data=data, db=db)

@router.get("/admin/users")
def list_all_users(db=Depends(get_db)):
    """
    List all users 
    """
    return user_service.get_users(db=db)


@router.post("/user/chatroom")
def create_chat_room(
    data: CreateChatRoomRequest,
    db=Depends(get_db),
):
    # return chat_room_service
    #@TODO: allow user to add other users while creating chat room -- time constraint
    return chat_room_service.create_chatroom(data=data,db=db) 

@router.post("/user/{user_id}/chatroom/add_users")
def add_users_to_chat_room(user_id:int,data:AddUserToChatRoomRequest, db=Depends(get_db)):
    #Add users to chat room
    return chat_room_service.add_users_to_chatroom(data=data,db=db)

@router.get("/user/{user_id}/chatroom")
def view_chat_rooms(user_id:int,db=Depends(get_db)):
    #Returns all chat rooms
    return chat_room_service.view_user_chat_rooms(user_id=user_id,db=db)

@router.get("/admin/chatrooms")
def view_all_chat_rooms(db=Depends(get_db)):
    #Returns all chat rooms
    return chat_room_service.view_all_chat_rooms(db=db)


@router.get("/admin/userchatrooms")
def view_all_user_chat_rooms(db=Depends(get_db)):
    # Returns all chat rooms where the user is present
    return chat_room_service.view_all_user_chat_rooms(db=db)

@router.post("/user/send_message")
def send_group_message(data: SendGroupMessageRequest, db=Depends(get_db)):
    #Sends message to a group 
    return chat_message_service.send_group_message(data=data,db=db)

@router.get("/admin/view_all_group_messages")
def view_all_group_messages(db=Depends(get_db)):
    #Sends message to a group 
    return chat_message_service.view_all_messages(db=db)
### Running this code

#### Install fast api

"pip install "fastapi[standard]""
extra requirements in requirement.txt file

#### Run migrations

"alembic upgrade head"

#### Start code

"fastapi dev main.py"

### Thought process

#### Models

User , ChatRoom , ChatMessage models will be created. see schema.py

#### Actions

User can be created
User can create ChatRoom
User can add one or more Users to ChatRoom
User in a ChatRoom can send message to the Chatroom
User(admin) can remove others from a ChatRoom
User can make others admin

##### random tjhoughts

model between user and chatroom

### Extras to be done

User id specific queries
Proper responses
Proper error messages
Writing unit tests
User authentication

other things in Ctr + F ( TODO)

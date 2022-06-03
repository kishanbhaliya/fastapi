from fastapi import FastAPI, Body, Depends
from app.models import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer

app = FastAPI()

posts = [
    {
        "id":1,
        "title": "Hello",
        "content": "hello there..."
    }
]

users = []


@app.get("/posts", tags=["posts"])
def get_posts() -> dict:
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with suplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
def add_post(post:PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


@app.post("/user/signup", tags=["user"])
def create_user(user: UserSchema = Body()):
    users.append(user) #replace with db call, making sure to hash the password first
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body()):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }
    
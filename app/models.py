from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field()
    content: str = Field()

    class Config:
        schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "In this tutorial, you will learn how to secure your application by enabling authentication using JWT. We'll be using PyJWT to sign, encode and decode JWT tokens...."
            }
        }


# User Registration and Log-in
class UserSchema(BaseModel):
    fullname: str = Field()
    email: EmailStr = Field()
    password: str = Field()

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Team Unibrains",
                "email": "unibrains@gmail.com",
                "password": "admin"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field()
    password: str = Field()

    class Config:
        schema_extra = {
            "exapmle": {
                "email": "unibrains@gmail.com",
                "password": "admin"
            }
        }
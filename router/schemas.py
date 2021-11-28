from pydantic import BaseModel, validator, EmailStr
from typing import List


class ProductRequestSchema(BaseModel):
    article_title: str
    author: str
    article_content: str
    owner_id: int


class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool


class OnlyUserResponseSchema(UserRequestSchema):
    pass

    class Config:
        orm_mode = True


class ProductResponseSchema(ProductRequestSchema):
    id: int
    owner_id: int
    owner: OnlyUserResponseSchema

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_admin: bool


class UserRequestSchema(UserBase):
    password1: str
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator("password1")
    def password_must_have_6_digits(cls, v):
        if len(v) < 6:
            raise ValueError("Password must have at least 6 digits")
        return v

class UserResponseSchema(UserRequestSchema):
    id: int
    created_products: List[ProductResponseSchema] = []

    class Config:
        orm_mode = True


from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    owner_id: int

class ArticleResponseSchema(ArticleRequestSchema):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserRequestSchema(BaseModel):
    username: str
    email: str

class UserResponseSchema(UserRequestSchema):
    id: int

    class Config:
        orm_mode = True

class OnlyUserResponseSchema(UserRequestSchema):
    pass

    class Config:
        orm_mode = True

class OnlyArticleResponseSchema(ArticleRequestSchema):
    pass

    class Config:
        orm_mode = True

class ArticleResponseWithUserSchema(ArticleRequestSchema):
    id: int
    owner_id: int
    owner: OnlyUserResponseSchema

    class Config:
        orm_mode = True

class UserResponseWithProductsSchema(UserRequestSchema):
    id: int
    created_articles: List[OnlyArticleResponseSchema] = []

    class Config:
        orm_mode = True


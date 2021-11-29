from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    title: str
    author: str
    content: str
    owner_id: int


class UserRequestSchema(BaseModel):
    username: str
    email: str


class OnlyUserResponseSchema(UserRequestSchema):
    pass

    class Config:
        orm_mode = True

class OnlyArticleResponseSchema(ArticleRequestSchema):
    pass

    class Config:
        orm_mode = True

class ArticleResponseSchema(ArticleRequestSchema):
    id: int
    owner_id: int
    owner: OnlyUserResponseSchema

    class Config:
        orm_mode = True

class UserResponseSchema(UserRequestSchema):
    id: int
    created_articles: List[OnlyArticleResponseSchema] = []

    class Config:
        orm_mode = True


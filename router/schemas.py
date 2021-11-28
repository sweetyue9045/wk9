from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    article_title: str
    author: str
    article_content: str
    owner_id: int


class UserRequestSchema(BaseModel):
    username: str
    email: str


class OnlyUserResponseSchema(UserRequestSchema):
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
    created_articles: List[ArticleResponseSchema] = []

    class Config:
        orm_mode = True


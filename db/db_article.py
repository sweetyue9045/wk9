from fastapi import HTTPException, status
from router.schemas import ProductRequestSchema
from sqlalchemy.orm.session import Session
from .article_feed import article

from db.models import DbArticle


def db_feed(db: Session):
    new_article_list = [DbArticle(
        article_title=article["article_title"],
        author=article["author"],
        article_content=article["article_content"],
        owner_id=article["owner_id"]
    ) for article in article]
    db.query(DbArticle).delete()
    db.commit()
    db.add_all(new_article_list)
    db.commit()
    return db.query(DbArticle).all()


def create(db: Session, request: ProductRequestSchema) -> DbArticle:
    new_product = DbArticle(
        article_title=request.article_title,
        author=request.author,
        article_content=request.article_content,
        owner_id=request.owner_id
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session) -> list[DbArticle]:
    return db.query(DbArticle).all()


def get_product_by_id(product_id: int, db: Session) -> DbArticle:
    product = db.query(DbArticle).filter(DbArticle.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Product with id = {id} not found')
    return product


# def get_product_by_category(category: str, db: Session) -> list[DbProduct]:
#     product = db.query(DbProduct).filter(DbProduct.category == category).all()
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f'Product with category = {id} not found')
#     return product

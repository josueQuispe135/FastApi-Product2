from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.products_category.models import ProductCategory
from app.products_category.schemas import ProductCategoryCreate, ProductCategoryUpdate


class ProductCategoryService:
    no_task:str = "Product doesn't exits"
    # CREATE
    # ----------------------
    def create_product_category(self, item_data: ProductCategoryCreate, session: SessionDep):
        item_db = ProductCategory.model_validate(item_data.model_dump())
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ONE
    # ----------------------
    def get_product_category(self, item_id: int, session: SessionDep):
        item_db = session.get(ProductCategory, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return item_db

    # UPDATE
    # ----------------------
    def update_product_category(self, item_id: int, item_data: ProductCategoryUpdate, session: SessionDep):
        item_db = session.get(ProductCategory, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        item_data_dict = item_data.model_dump(exclude_unset=True)
        item_db.sqlmodel_update(item_data_dict)
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ALL PLANS
    # ----------------------
    def get_product_categories(self, session: SessionDep):
        return session.exec(select(ProductCategory)).all()

    # DELETE
    # ----------------------
    def delete_product_category(self, item_id: int, session: SessionDep):
        item_db = session.get(ProductCategory, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        session.delete(item_db)
        session.commit()
        
        return {"detail": "ok"}

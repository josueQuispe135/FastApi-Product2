from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.products_brand.models import ProductBrand
from app.products_brand.schemas import ProductBrandCreate, ProductBrandUpdate


class ProductBrandService:
    no_task:str = "Brand doesn't exits"
    # CREATE
    # ----------------------
    def create_product_brand(self, item_data: ProductBrandCreate, session: SessionDep):
        item_db = ProductBrand.model_validate(item_data.model_dump())
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db

    # GET ONE
    # ----------------------
    def get_product_brand(self, item_id: int, session: SessionDep):
        item_db = session.get(ProductBrand, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return item_db

    # UPDATE
    # ----------------------
    def update_product_brand(self, item_id: int, item_data: ProductBrandUpdate, session: SessionDep):
        item_db = session.get(ProductBrand, item_id)
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
    def get_product_brands(self, session: SessionDep):
        return session.exec(select(ProductBrand)).all()

    # DELETE
    # ----------------------
    def delete_product_brand(self, item_id: int, session: SessionDep):
        item_db = session.get(ProductBrand, item_id)
        if not item_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        #print(f"Producto {item_db}")
        session.delete(item_db)
        session.commit()
        return {"detail": "ok"}

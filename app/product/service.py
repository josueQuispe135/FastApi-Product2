from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.product.models import Product
from app.product.schemas import ProductCreate, ProductUpdate




class ProductService:
    no_product:str = "Product doesn't exits"
    # CREATE
    # ----------------------
    def create_product(self, plan_data: ProductCreate, session: SessionDep):
        product_db = Product.model_validate(plan_data.model_dump())
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ONE
    # ----------------------
    def get_product(self, plan_id: int, session: SessionDep):
        product_db = session.get(Product, plan_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_product
            )
        return product_db

    # UPDATE
    # ----------------------
    def update_product(self, plan_id: int, plan_data: ProductUpdate, session: SessionDep):
        product_db = session.get(Product, plan_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_product
            )
        plan_data_dict = plan_data.model_dump(exclude_unset=True)
        product_db.sqlmodel_update(plan_data_dict)
        session.add(product_db)
        session.commit()
        session.refresh(product_db)
        return product_db

    # GET ALL PLANS
    # ----------------------
    def get_products(self, session: SessionDep):
        return session.exec(select(Product)).all()

    # DELETE
    # ----------------------
    def delete_product(self, plan_id: int, session: SessionDep):
        product_db = session.get(Product, plan_id)
        if not product_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_product
            )
        session.delete(product_db)
        session.commit()
        print("debería salir el mensaje")
        return {"detail": "ok"}

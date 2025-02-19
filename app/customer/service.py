from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.customer.models import Customer
from app.customer.schemas import CustomerCreate, CustomerUpdate




class CustomerService:
    no_customer:str = "Customer doesn't exits"
    # CREATE
    # ----------------------
    def create_customer(self, plan_data: CustomerCreate, session: SessionDep):
        customer_db = Customer.model_validate(plan_data.model_dump())
        session.add(customer_db)
        session.commit()
        session.refresh(customer_db)
        return customer_db

    # GET ONE
    # ----------------------
    def get_customer(self, plan_id: int, session: SessionDep):
        customer_db = session.get(Customer, plan_id)
        if not customer_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_customer
            )
        return customer_db

    # UPDATE
    # ----------------------
    def update_customer(self, plan_id: int, plan_data: CustomerUpdate, session: SessionDep):
        customer_db = session.get(Customer, plan_id)
        if not customer_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_customer
            )
        plan_data_dict = plan_data.model_dump(exclude_unset=True)
        customer_db.sqlmodel_update(plan_data_dict)
        session.add(customer_db)
        session.commit()
        session.refresh(customer_db)
        return customer_db

    # GET ALL PLANS
    # ----------------------
    def get_customers(self, session: SessionDep):
        return session.exec(select(Customer)).all()

    # DELETE
    # ----------------------
    def delete_customer(self, plan_id: int, session: SessionDep):
        customer_db = session.get(Customer, plan_id)
        if not customer_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_customer
            )
        session.delete(customer_db)
        session.commit()
        print("debería salir el mensaje")
        return {"detail": "ok"}

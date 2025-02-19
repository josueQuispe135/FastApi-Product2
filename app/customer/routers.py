
from fastapi import APIRouter, status

from app.db import SessionDep
from app.customer.models import Customer
from app.customer.schemas import CustomerCreate, CustomerUpdate
from app.customer.service import CustomerService

router = APIRouter()
service = CustomerService()


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def create_customer(
    customer_data: CustomerCreate,
    session: SessionDep
    ):
    return service.create_customer(customer_data, session)
# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{customer_id}", response_model=Customer)
async def get_customer(
    customer_id: int,
    session: SessionDep
):
    return service.get_customer(customer_id,session)

# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch("/{customer_id}", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def update_customer(
    customer_id: int,
    customer_data: CustomerUpdate,
    session: SessionDep
):
    
    return service.update_customer(customer_id, customer_data, session)

# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[Customer])
async def get_customers(
    session: SessionDep
):
    return service.get_customers(session)

# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{customer_id}")
async def delete_customer(
    customer_id: int,
    session: SessionDep,
):
    return service.delete_customer(customer_id, session)
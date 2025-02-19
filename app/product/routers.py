
from fastapi import APIRouter, status

from app.db import SessionDep
from app.product.models import Product
from app.product.schemas import ProductCreate, ProductUpdate
from app.product.service import ProductService

router = APIRouter()
service = ProductService()


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    session: SessionDep
    ):
    return service.create_product(product_data, session)
# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: int,
    session: SessionDep
):
    return service.get_product(product_id,session)

# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch("/{product_id}", response_model=Product, status_code=status.HTTP_201_CREATED)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    session: SessionDep
):
    
    return service.update_product(product_id, product_data, session)

# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[Product])
async def get_products(
    session: SessionDep
):
    return service.get_products(session)

# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    session: SessionDep,
):
    return service.delete_product(product_id, session)
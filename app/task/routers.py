
from fastapi import APIRouter, status

from app.db import SessionDep
from app.task.models import Task
from app.task.schemas import TaskCreate, TaskUpdate
from app.task.service import TaskService

router = APIRouter()
service = TaskService()


# CREATE - Crear una nueva tarea
# ----------------------
@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    session: SessionDep
    ):
    return service.create_task(task_data, session)
# GET ONE - Obtener una tarea por ID
# ----------------------
@router.get("/{task_id}", response_model=Task)
async def get_task(
    task_id: int,
    session: SessionDep
):
    return service.get_task(task_id,session)

# UPDATE - Actualizar una tarea existente
# ----------------------
@router.patch("/{task_id}", response_model=Task, status_code=status.HTTP_201_CREATED)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    session: SessionDep
):
    
    return service.update_task(task_id, task_data, session)

# GET ALL TASK - Obtener todas las tareas
# ----------------------
@router.get("/", response_model=list[Task])
async def get_tasks(
    session: SessionDep
):
    return service.get_tasks(session)

# DELETE - Eliminar una tarea
# ----------------------
@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    session: SessionDep,
):
    return service.delete_task(task_id, session)
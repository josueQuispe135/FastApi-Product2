from fastapi import HTTPException, status
from sqlmodel import select

from app.db import SessionDep
from app.task.models import Task
from app.task.schemas import TaskCreate, TaskUpdate




class TaskService:
    no_task:str = "Task doesn't exits"
    # CREATE
    # ----------------------
    def create_task(self, plan_data: TaskCreate, session: SessionDep):
        task_db = Task.model_validate(plan_data.model_dump())
        session.add(task_db)
        session.commit()
        session.refresh(task_db)
        return task_db

    # GET ONE
    # ----------------------
    def get_task(self, plan_id: int, session: SessionDep):
        task_db = session.get(Task, plan_id)
        if not task_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        return task_db

    # UPDATE
    # ----------------------
    def update_task(self, plan_id: int, plan_data: TaskUpdate, session: SessionDep):
        task_db = session.get(Task, plan_id)
        if not task_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        plan_data_dict = plan_data.model_dump(exclude_unset=True)
        task_db.sqlmodel_update(plan_data_dict)
        session.add(task_db)
        session.commit()
        session.refresh(task_db)
        return task_db

    # GET ALL PLANS
    # ----------------------
    def get_tasks(self, session: SessionDep):
        return session.exec(select(Task)).all()

    # DELETE
    # ----------------------
    def delete_task(self, plan_id: int, session: SessionDep):
        task_db = session.get(Task, plan_id)
        if not task_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=self.no_task
            )
        session.delete(task_db)
        session.commit()
        print("debería salir el mensaje")
        return {"detail": "ok"}

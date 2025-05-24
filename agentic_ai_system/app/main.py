from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import Optional
from app.agents.coordinator import CoordinatorAgent
from app.utils.task_manager import TaskManager

app = FastAPI()
task_manager = TaskManager()

class ExecuteRequest(BaseModel):
    request: str
    require_approval: bool = False

@app.post("/api/v1/execute")
async def execute(req: ExecuteRequest):
    task_id = str(uuid4())
    plan, status = await CoordinatorAgent.plan_task(req.request, req.require_approval)
    task_manager.add_task(task_id, plan, status)

    if status == "waiting_approval":
        return {"task_id": task_id, "status": status, "plan": plan}
    else:
        result = await CoordinatorAgent.execute_plan(plan)
        task_manager.complete_task(task_id, result)
        return {"task_id": task_id, "status": "completed", **result}

@app.post("/api/v1/plans/{task_id}/approve")
async def approve(task_id: str):
    plan = task_manager.get_plan(task_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Task not found")
    result = await CoordinatorAgent.execute_plan(plan)
    task_manager.complete_task(task_id, result)
    return {"task_id": task_id, "status": "completed", **result}

@app.post("/api/v1/plans/{task_id}/reject")
async def reject(task_id: str):
    task_manager.fail_task(task_id, reason="User rejected the plan")
    return {"task_id": task_id, "status": "rejected"}

@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: str):
    task = task_manager.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
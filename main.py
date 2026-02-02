from fastapi import FastAPI
from tasks import train_ml_model, run_command, transform_data
from celery_app import celery
app = FastAPI()

@app.post("/train")
def start_ml_training():
    task = train_ml_model.delay({"sample": "data"})
    return {"task_id": task.id}

@app.post("/execute")
def execute_command(command: str):
    task = run_command.delay(command)
    return {"task_id": task.id}

@app.post("/transform")
def start_data_transformation():
    sample_data = [{"value": 10}, {"value": 20}, {"value": 30}]
    task = transform_data.delay(sample_data)
    return {"task_id": task.id}

@app.get("/status/{task_id}")
def get_task_status(task_id: str):
    task = celery.AsyncResult(task_id)
    return {"status": task.status}

@app.get("/result/{task_id}")
def get_task_result(task_id: str):
    task = celery.AsyncResult(task_id)
    return {"result": task.result if task.ready() else None}
from celery_app import celery
import time

@celery.task
def train_ml_model(data):
    time.sleep(10)
    return {"status": "ML model trained"}

@celery.task
def run_command(command):
    import subprocess
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout.decode()

@celery.task
def transform_data(data):
    transformed = [d['value'] * 2 for d in data]
    return transformed
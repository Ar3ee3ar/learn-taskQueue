from dotenv import load_dotenv
import os
from celery import Celery

load_dotenv()

celery = Celery(
    'worker',
    broker=os.getenv('CELERY_BROKER_URL'),
    backend=os.getenv('CELERY_BACKEND_URL'),
    include=['tasks']
)
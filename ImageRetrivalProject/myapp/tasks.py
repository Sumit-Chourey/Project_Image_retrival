# myapp/tasks.py
from celery import shared_task
from PIL import Image
import os
from django.conf import settings

@shared_task
def optimize_image(image_path, optimized_path):
    with Image.open(image_path) as img:
        img.save(optimized_path, optimize=True, quality=85)
    return optimized_path

import os
from django.conf import settings
from django.db import models

# Create your models here.
# myapp/models.py
from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    optimized_image = models.ImageField(upload_to='optimized_images/', null=True, blank=True)


    @property
    def optimized_image_path(self):
        return os.path.join(settings.MEDIA_ROOT, 'optimized_images', os.path.basename(self.image.name))

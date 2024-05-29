from django.urls import path

from .views import  get_images, upload_image


urlpatterns = [
    
    
    path('upload/', upload_image),
   
   # path('getbyid/<int:image_id>/',retrieve_image_byId),
    path('get/', get_images)
    
]
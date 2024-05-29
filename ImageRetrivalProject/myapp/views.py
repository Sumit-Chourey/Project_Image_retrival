from django.shortcuts import render

# Create your views here.
# myapp/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .tasks import optimize_image
from .models import ImageModel

@api_view(['POST'])
def upload_image(request):
    if 'image' not in request.FILES:
        return JsonResponse({'error': 'No image found in request'}, status=400)
    
    image_file = request.FILES['image']
    image_instance = ImageModel.objects.create(image=image_file)
    optimize_image.delay(image_instance.image.path, image_instance.optimized_image_path)
    
    return JsonResponse({'message': 'Image uploaded successfully'}, status=201)



#get request 

from django.http import JsonResponse
from .models import ImageModel

@api_view(['GET'])
def get_images(request):
    images = ImageModel.objects.all()
    image_data = []
    for image in images:
        image_info = {
            'image_url': image.image.url
        }
        if image.optimized_image:  # Check if optimized_image exists
            image_info['optimized_image_url'] = image.optimized_image.url
        image_data.append(image_info)
    return JsonResponse({'images': image_data})

    
"""
# Get request for by images by id

@api_view(['GET'])
def retrieve_image_byId(request, image_id):
    try:
        image_instance = ImageModel.objects.get(id=image_id)
    except ImageModel.DoesNotExist:
        return JsonResponse({'error': 'Image not found'}, status=404)

    return JsonResponse({'image_url': image_instance.image.url, 'optimized_image_url': image_instance.optimized_image.url})
"""

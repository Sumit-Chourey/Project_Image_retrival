"""
URL configuration for ImageRetrivalProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pstats import Stats
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
# from ImageRetrivalProject.myapp.views import retrieve_image, upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('myapp.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
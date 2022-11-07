from . import views
from django.urls import path

urlpatterns = [
    path('image', views.upload_image, name='image'),
    path('file', views.upload_file, name='upload_file')
]
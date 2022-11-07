#app/urls.py

from django.urls import path

#as advised from https://medium.datadriveninvestor.com/python-django-views-templates-models-f0844a00db70
from . import views
#from app.views import *
#app is the current directory so a . instead of app would also work
from app import views
#the subpath for 'job/' is dynamically assigned with <id> variable
#the <id> variable need be captured in the views job_detail function
#adding the int: in front of the id variable will
#This path pattern  
#    path('templates/app', views.hello, name='hello'),
# can reveal the page with this url
# http://127.0.0.1:8000/templates/app   

#This path pattern  
#    path('templates/app', views.hello, name='hello'),
# can reveal the page with this url http://127.0.0.1:8000/hello  


urlpatterns = [
    path('', views.jobs, name='jobs_home'),
    path('hello/', views.hello, name='hello'),
    path('job/<int:id>', views.job_detail, name='job_detail'),
    # path('job_detail/<int:id>', views.job_detail, name='job_detail'),
]
#path('job/<int:id>', views.job_detail)
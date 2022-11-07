from typing import List
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.template import loader

from app.models import JobPost

# Create your views here.
#a view is Python function which takes a request and returns a function
#HttpResponse is a class
#the HttpResponse class is returned by the hello function below

class TempClass:
    x=5

class Demographics:
    age = 30

def hello(request):
#the following template variable can be compressed usin the function render(<render object>, <template>,<context>)
    #template=loader.get_template('app/hello.html')
    list = ["alpha", "beta"]
    list2 = {1: "apple", 2: "pear", '3': "banana"}
    temp = TempClass()
    is_authenticated = True
    age = Demographics.age
    context = {"addressee": "Jacko", "first_list": list, "len_list" : len(list), "is_authenticated": is_authenticated, "fruit": list2}
    try:
        return render(request(context, request))
#        return render(request, "app/hello.html", context)
        #return_html =f"Hello'<br>{list[0]}<br>"
        # return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("hello world template file not found or won't render due to error")


job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description =[
    "First Job Description",
    "Second Job Description",
    "Third Job Description"
]

# def about(request):
#     try:
#         return render(request, "app/about.html")
#     except:
#         return HttpResponseNotFound("Couldn't load 'about' page")

def jobs(request):
  # fetch all job posts from data base
    jobs = JobPost.objects.all()
    
    context = {"jobs": jobs}
    try:
        return render(request, "app/index.html", context)
        #return HttpResponseNotFound("Job list Got this far")
    except Exception as e:
        print(e)
        return HttpResponseNotFound("Job list Not Found")        

def job_detail(request, id):

    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        job=JobPost.objects.get(id=id)
        context = {"job": job}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
from typing import List
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.template import loader

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
#    context = {"addressee": "Jacko", "first_list": list, "fruit": list2, "age": age, "temp_object": temp, "is_authenticated": is_authenticated}
    context = {"addressee": "Jacko", "first_list": list, "len_list" : len(list), "is_authenticated": is_authenticated, "fruit": list2}
#    context = {"addressee": "Jacko"}
    try:
#        return HttpResponse(template.render(context, request))
        return render(request, "app/hello.html", context)
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

def jobs(request):
    return_html="<ul>"
    for item in job_title:
        job_id = job_title.index(item)
        #print("\njob detail in reverse ", reverse('job_detail', args=(job_id,)))
        #replace the href='job/{job_id}' with variable taking the reverse('job_detail')
        url_job_call=reverse('job_detail', args=(job_id,))
        #return_html += f"<li><a href='job/{job_id}'>{item}</a></li><br>"
        return_html += f"<li><a href='{url_job_call}'>{item}</a></li><br>"
    return_html += "</ul>"
    return HttpResponse(return_html)

def job_detail(request, id):
    #return HttpResponse(f"<h3>Job detail page {id}</h3>")
    #site="https://google.com"
    #return HttpResponse(f"Visit <a href={site}>Google here</a>")
    #print(f"******\njob title: {job_title} and id {id} \n***id is of type {type(id)}**\n")
    context = {"job_title": job_title[id], "job_description" : job_description[id]}

    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        context={"job_title":job_title[id], "job_description":job_description[id]}
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Not Found")
        # if id > len(job_title)-1:
        #     return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1><h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        #return render(request, "app/job_detail.html", context)
from unittest.util import _MAX_LENGTH
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify
# Every model defined in Django is a subclass of django.db.models.Model
# migration commands include
# makemigrations: creates new migrations on changes identified in models
#   when running python manage.py makemigrations Django looks to the web project's settings.py
#   there it ought to find under INSTALLED_APPS
#   'app.apps.AppConfig' where app is the name of our app
#   the file created 'app/0001_initial.py' automatically adds an ID field
# sqlmigrate: displays the SQL statement for a migration
#   python manage.py sqlmigrate app 0001 will display the SQL that creates the table from the model
#   migrate: runs, applies, and unapplies migrations
# showmigrations: lists the migrations of projects along with their status

class Skills(models.Model):
    name = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)


class Location(models.Model):
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=12)

# the max length of SlugField is 50 by default
class JobPost(models.Model):
    JOB_TYPE_CHOICES =[
        ('Permanent Full Time', 'F/T'),
        ('Permanent Part Time', 'P/T'),
        ('Fixed Contract', 'Cntr')
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique=True)
    location = models.OneToOneField(Location, null=True, on_delete = models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='jobpost', related_query_name='jobposts')
    skill = models.ManyToManyField(Skills)
    type = models.CharField(max_length=200, null=False, choices=JOB_TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} with salary {self.salary}"


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)
    

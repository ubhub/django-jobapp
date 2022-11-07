from django.contrib import admin
from app.models import JobPost, Location, Author, Skills

class JobAdmin(admin.ModelAdmin):
    #list_display = ('__str__', 'date')
    list_display = ('title', 'salary', 'date', 'expiry')
    list_filter = ('date', 'salary', 'expiry')
    # the search field can be a tuple or list; same for filter I think
    search_fields = ('title', 'description')
    search_help_text="Search by any text found in title or description. (Search isn't case sensitive)"
    #fields = (('title', 'salary'), 'description')
    #exclude = ('expiry',)
    fieldsets = (
        ('job title', {
        'fields': ('title', 'description')
        }),
        ('More information', {
        'classes':('collapse'),
        'fields': (('salary', 'expiry'),'slug')
        }),
    )

# Register your models here.
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
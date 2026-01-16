from django.contrib import admin

# Register your models here.
from escola.models import Estudent, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'document', 'birth', 'phone')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name', 'email', 'document')
    ordering = ('name',)

admin.site.register(Estudent, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'duration', 'price', 'nivel')
    list_display_links = ('id', 'name', 'description')
    list_per_page = 20
    search_fields = ('name', 'description', 'nivel')

admin.site.register(Course, Courses)

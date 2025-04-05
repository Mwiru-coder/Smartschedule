from django.contrib import admin
from .models import Department, Program, Course,Instructor, Group, Schedule, Conflict


# Register your models here.

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(Conflict)

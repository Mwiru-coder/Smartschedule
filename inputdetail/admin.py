from django.contrib import admin
from .models import Venue, Department, Program, Course,User, Group, Schedule, Conflict


# Register your models here.

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Venue)
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(Conflict)

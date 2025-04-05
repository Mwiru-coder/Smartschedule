from .models import Program, Department, Course, User,Conflict, Venue, Group, Schedule
from graphene_django import DjangoObjectType
from django.contrib import admin
# from django.utils.translation import gettext_lazy as _

class ProgramType(DjangoObjectType):
    class Meta:
        model = Program
        fields = "__all__"


class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department
        fields ="__all__"


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"

class ConflictType(DjangoObjectType):
    class Meta:
        model = Conflict
        fields = "__all__"  

class VenueType(DjangoObjectType):
    class Meta:
        model = Venue
        fields = "__all__"

class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = "__all__"

class ScheduleType(DjangoObjectType):
    class Meta:
        model = Schedule
        fields = "__all__"
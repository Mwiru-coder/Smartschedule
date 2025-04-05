import graphene
from ..models import Course
from ..Objecttype import CourseType

class Course(graphene.ObjectType):
    Course = graphene.List(CourseType)
    def resolve_course(self, info,):
        return Course.objects.all()

class Query(graphene.ObjectType):
    pass
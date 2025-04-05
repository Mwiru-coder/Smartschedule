import graphene
from ..models import Course
from ..Objecttype import CourseType

class AddCourse(graphene.Mutation):
    class Arguments:
        Course_name = graphene.String(required=True)
        Course_code = graphene.String(required=True)
        Course_credit = graphene.Int(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, Course_name, Course_code, Course_credit):
        try:
            new_course = Course(
                course_name=Course_name,
                course_code=Course_code,
                course_credit=Course_credit,
            )
            new_course.save()
            return AddCourse(success=True, message="Course added successfully.")
        except Exception as error:
            return AddCourse(success=False, message=str(error))
    


class UpdateCourse(graphene.Mutation):
    class Arguments:
        Course_name = graphene.String(required=True)
        Course_code = graphene.String(required=True)
        Course_credit = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, Course_name, Course_code, Course_credit):
        try:
            course = Course.objects.get(course_code=Course_code)
            course.course_name = Course_name
            course.course_credit = Course_credit
            course.save()
            return UpdateCourse(success=True, message="Course updated successfully.")
        except Course.DoesNotExist:
            return UpdateCourse(success=False, message="Course not found.")
        except Exception as error:
            return UpdateCourse(success=False, message=str(error))
        
    
class DeleteCourse(graphene.Mutation):
    class Arguments:
        Course_code = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, Course_code):
        try:
            course = Course.objects.get(course_code=Course_code)
            course.delete()
            return DeleteCourse(success=True, message="Course deleted successfully.")
        except Course.DoesNotExist:
            return DeleteCourse(success=False, message="Course not found.")
        except Exception as error:
            return DeleteCourse(success=False, message=str(error))
        


class Mutation(graphene.ObjectType):
    add_course = AddCourse.Field()
    update_course = UpdateCourse.Field()
    delete_course = DeleteCourse.Field()
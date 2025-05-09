import graphene
from inputdetail.models import Course


class AddCourse(graphene.Mutation):
    class Arguments:
        course_name = graphene.String(required=True)
        course_code = graphene.String(required=True)
        course_credit = graphene.Int(required=True)
        program_code = graphene.String(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, course_name, course_code, course_credit,program_code):
        try:
            new_course = Course(
                course_name=course_name,
                course_code=course_code,
                course_credit=course_credit,
                program_code = program_code
            )
            new_course.save()
            return AddCourse(success=True, message="Course added successfully.")
        except Exception as error:
            return AddCourse(success=False, message=str(error))
    


class UpdateCourse(graphene.Mutation):
    class Arguments:
        course_name = graphene.String(required=True)
        course_code = graphene.String(required=True)
        course_credit = graphene.Int(required=True)
        program_code = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, course_name, course_code,course_credit, program_code):
        try:
            course = Course.objects.get(course_code=course_code)
            course.course_name = course_name
            course.course_credit = course_credit
            course.program_code = program_code
            course.save()
            return UpdateCourse(success=True, message="Course updated successfully.")
        except Course.DoesNotExist:
            return UpdateCourse(success=False, message="Course not found.")
        except Exception as error:
            return UpdateCourse(success=False, message=str(error))
        
    
class DeleteCourse(graphene.Mutation):
    class Arguments:
        course_code = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, course_code):
        try:
            course = Course.objects.get(course_code=course_code)
            course.delete()
            return DeleteCourse(success=True, message="Course deleted successfully.")
        except Course.DoesNotExist:
            return DeleteCourse(success=False, message="Course not found.")
        except Exception as error:
            return DeleteCourse(success=False, message=str(error))
        


# class Mutation(graphene.ObjectType):
#     add_course = AddCourse.Field()
#     update_course = UpdateCourse.Field()
#     delete_course = DeleteCourse.Field()
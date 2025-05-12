import graphene
from inputdetail.models import Course, Program

class AddCourse(graphene.Mutation):
    class Arguments:
        courseName = graphene.String(required=True)
        courseCode = graphene.String(required=True)
        courseCredit = graphene.Int(required=True)
        programCode = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, courseName, courseCode, courseCredit, programCode):
        try:
            # Check if the course code already exists
            if Course.objects.filter(course_code=courseCode).exists():
                return AddCourse(success=False, message="Course with this code already exists.")
            # Check if the course name already exists
            if Course.objects.filter(course_name=courseName).exists():
                return AddCourse(success=False, message="Course with this name already exists.")

            # Retrieve the Program using programCode
            program = Program.objects.get(program_code=programCode)

            # Create the new Course
            Course.objects.create(
                course_code=courseCode,
                course_name=courseName,
                course_credit=courseCredit,
                program_code=program  # ForeignKey to Program
            )

            return AddCourse(success=True, message="Course added successfully.")
        except Program.DoesNotExist:
            return AddCourse(success=False, message="Program not found.")
        except Exception as error:
            return AddCourse(success=False, message=str(error))


class UpdateCourse(graphene.Mutation):
    class Arguments:
        courseName = graphene.String(required=True)
        courseCode = graphene.String(required=True)
        courseCredit = graphene.Int(required=True)
        programCode = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, courseName, courseCode, courseCredit, programCode):
        try:
            # Get the existing Course by course_code
            course = Course.objects.get(course_code=courseCode)

            # Get the Program instance using programCode
            program = Program.objects.get(program_code=programCode)

            # Update the course fields
            course.course_name = courseName
            course.course_credit = courseCredit
            course.program_code = program  # ForeignKey to Program
            course.save()

            return UpdateCourse(success=True, message="Course updated successfully.")
        except Course.DoesNotExist:
            return UpdateCourse(success=False, message="Course not found.")
        except Program.DoesNotExist:
            return UpdateCourse(success=False, message="Program not found.")
        except Exception as error:
            return UpdateCourse(success=False, message=str(error))


class DeleteCourse(graphene.Mutation):
    class Arguments:
        courseCode = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, courseCode):
        try:
            # Get the course by course_code
            course = Course.objects.get(course_code=courseCode)
            course.delete()
            return DeleteCourse(success=True, message="Course deleted successfully.")
        except Course.DoesNotExist:
            return DeleteCourse(success=False, message="Course not found.")
        except Exception as error:
            return DeleteCourse(success=False, message=str(error))


# Register the mutations
class Mutation(graphene.ObjectType):
    add_course = AddCourse.Field()
    update_course = UpdateCourse.Field()
    delete_course = DeleteCourse.Field()

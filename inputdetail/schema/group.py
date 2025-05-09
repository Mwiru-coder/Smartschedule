import graphene

from inputdetail.schema import Department, course
from ..models import Course, Group, Program


class AddGroup(graphene.Mutation):
    class Arguments:
        group_id = graphene.Int(required=True)
        group_name = graphene.String(required=True)
        academic_year = graphene.String(required=True)
        course_code = graphene.String(required=True)
        program_code = graphene.String(required=True)
        student_No = graphene.Int(required=True)
        department_id = graphene.String(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()
    def mutate(root, info, group_id, group_name, academic_year, course_code, program_code, student_No, department_id):
        try:
            # Check if the course code exists in the Course model
            course = Course.objects.get(course_code=course_code)
            program = Program.objects.get(program_code=program_code)
            department = Department.objects.get(department_id=department_id)
            new_group = Group(
                group_id=group_id,
                group_name=group_name,
                academic_year=academic_year,
                department_id=department,
                program_code=program,
                course_code=course,
                student_No= student_No,
            )
            new_group.save()
            return AddGroup(success=True, message="Group added successfully.")
        except Exception as error:
            return AddGroup(success=False, message=str(error))

class UpdateGroup(graphene.Mutation):
    class Arguments:
        group_id = graphene.Int(required=True)
        group_name = graphene.String(required=True)
        academic_year = graphene.String(required=True)
        course_code = graphene.String(required=True)
        program_code = graphene.String(required=True)
        student_No = graphene.Int(required=True)
        department_id = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, group_id, group_name, academic_year, course_code, program_code,  student_No, department_id):
        try:
            # Check if the course code exists in the Course model
            course = Course.objects.get(course_code=course_code)
            program = Program.objects.get(program_code=program_code)
            department = Department.objects.get(department_id=department_id)

            group = Group.objects.get(group_id=group_id),
            group.group_name = group_name,
            group.academic_year = academic_year,
            group.course_code = course,
            program_code = program,
            department = department,
            group.program_code = program_code,
            group. student_No= student_No,
            group.save()
            return UpdateGroup(success=True, message="Group updated successfully.")
        except Group.DoesNotExist:
            return UpdateGroup(success=False, message="Group not found.")
        except Exception as error:
            return UpdateGroup(success=False, message=str(error))

class DeleteGroup(graphene.Mutation):
    class Arguments:
        group_id = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, group_id):
        try:
            group = Group.objects.get(group_id=group_id)
            group.delete()
            return DeleteGroup(success=True, message="Group deleted successfully.")
        except Group.DoesNotExist:
            return DeleteGroup(success=False, message="Group not found.")
        except Exception as error:
            return DeleteGroup(success=False, message=str(error))
        


# class Mutation(graphene.ObjectType):
#     add_group = AddGroup.Field()
#     update_group = UpdateGroup.Field()
#     delete_group = DeleteGroup.Field()
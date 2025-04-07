import graphene
from ..models import Group


class AddGroup(graphene.Mutation):
    class Arguments:
        group_id = graphene.Int(required=True)
        group_name = graphene.String(required=True)
        academic_year = graphene.String(required=True)
        course_code = graphene.String(required=True)
        program_code = graphene.String(required=True)
        student_number = graphene.Int(required=True)
        department_id = graphene.String(required=True)
    
    success = graphene.Boolean()
    message = graphene.String()
    def mutate(root, info, group_id, group_name, academic_year, course_code, program_code, student_number, department_id):
        try:
            new_group = Group(
                group_id=group_id,
                group_name=group_name,
                academic_year=academic_year,
                course_code=course_code,
                program_code=program_code,
                student_number=student_number,
                department_id=department_id
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
        student_number = graphene.Int(required=True)
        department_id = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, group_id, group_name, academic_year, course_code, program_code, student_number, department_id):
        try:
            group = Group.objects.get(group_id=group_id)
            group.group_name = group_name
            group.academic_year = academic_year
            group.course_code = course_code
            group.program_code = program_code
            group.student_number = student_number
            group.department_id = department_id
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
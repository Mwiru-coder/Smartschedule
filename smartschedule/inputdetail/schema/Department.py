import graphene
from inputdetail.models import Department

class AddDepartment(graphene.Mutation):
    class Arguments:
        department_name = graphene.String(required=True)
        department_id = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root,info,department_name,department_id):
        try:
            new_department = Department(
                department_name=department_name,
                department_id=department_id,
            )
            new_department.save()
            return AddDepartment(success=True, message="Department added successfully.")
        except Exception as error:
            return AddDepartment(success=False, message=str(error))
        
    

class UpdateDepartment(graphene.Mutation):
    class Arguments:
        department_name = graphene.String(required=True)
        department_id = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root,info,department_name,department_id):
        try:
            department = Department.objects.get(department_id=department_id)
            department.department_name = department_name
            department.save()
            return UpdateDepartment(success=True, message="Department updated successfully.")
        except Department.DoesNotExist:
            return UpdateDepartment(success=False, message="Department not found.")
        except Exception as error:
            return UpdateDepartment(success=False, message=str(error))
        
    
class DeleteDepartment(graphene.Mutation):
    class Arguments:
        department_id = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root, info, department_id):
        try:
            department = Department.objects.get(department_ide=department_id)
            department.delete()
            return DeleteDepartment(success=True, message="Department deleted successfully.")
        except Department.DoesNotExist:
            return DeleteDepartment(success=False, message="Department not found.")
        except Exception as error:
            return DeleteDepartment(success=False, message=str(error))
        


# class Mutation(graphene.ObjectType):
#     add_department = AddDepartment.Field()
#     update_department = UpdateDepartment.Field()
#     delete_department = DeleteDepartment.Field()
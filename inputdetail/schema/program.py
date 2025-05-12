import graphene
from ..models import Program, Department


# mutation kwa ajili ya kuongeza taarifa za programe
class AddProgram(graphene.Mutation):
    class Arguments:
        program_name = graphene.String(required=True)
        program_code = graphene.String(required=True)
        duration = graphene.String(required=True)
        department_id = graphene.ID(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, program_name, program_code,duration, department_id):
        try:
            department=Department.objects.get(department_id=department_id)
            Program.objects.create(
                department_id=department,
                program_name=program_name,
                program_code=program_code,
                duration=duration
            )
            return AddProgram(success=True, message="Program added successfully.")
        except Program.DoesNotExist:
            return AddProgram(success=False, message="Department not found.")
        except Exception as error:
            return AddProgram(success=False, message=str(error))


    
# mutation kwa ajili ya kuhariri taarifa za program
class UpdateProgram(graphene.Mutation):
    class Arguments:
        program_name = graphene.String(required=True)
        program_code = graphene.String(required=True)
        duration = graphene.String(required=True)
        department_id = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info,program_name, program_code,duration,department_id):
        try:
            program = Program.objects.get(program_code=program_code)
            program.program_name = program_name
            program.duration = duration
            program.department_id = department_id
            program.save()
            return UpdateProgram(success=True, message="Program updated successfully.")
        except Program.DoesNotExist:
            return UpdateProgram(success=False, message="That Department not found.")
        except Exception as error:
            return UpdateProgram(success=False, message=str(error))

# mutation kwa ajili ya kufuta taarifa za program
class DeleteProgram(graphene.Mutation):
    class Arguments:
        program_code = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, program_code):
        try:
            program = Program.objects.get(program_code=program_code)
            program.delete()
            return DeleteProgram(success=True, message="Program deleted successfully.")
        except Program.DoesNotExist:
            return DeleteProgram(success=False, message="Program not found.")
        except Exception as e:
            return DeleteProgram(success=False, message=str(e))
    
# class Mutation(graphene.ObjectType):
#     add_program = AddProgram.Field()
#     update_program = UpdateProgram.Field()
#     delete_program = DeleteProgram.Field()
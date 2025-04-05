import graphene
from ..models import Program
from ..Objecttype import ProgramType


# mutation kwa ajili ya kuongeza taarifa za programe
class AddProgram(graphene.Mutation):
    class Arguments:
        program_name = graphene.String(required=True)
        program_code = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, program_name, program_code,):
        try:
            new_program = Program(
                program_name=program_name,
                program_code=program_code,
            )
            new_program.save()
            return AddProgram(success=True, message="Program added successfully.")
        except Exception as e:
            return AddProgram(success=False, message=str(e))
        
    
# mutation kwa ajili ya kuhariri taarifa za program
class UpdateProgram(graphene.Mutation):
    class Arguments:
        program_name = graphene.String(required=True)
        program_code = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info,program_name, program_code):
        try:
            program = Program.objects.get(id=program_code)
            program.program_name = program_name
            program.save()
            return UpdateProgram(success=True, message="Program updated successfully.")
        except Program.DoesNotExist:
            return UpdateProgram(success=False, message="Program not found.")
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
            program = Program.objects.get(id=program_code)
            program.delete()
            return DeleteProgram(success=True, message="Program deleted successfully.")
        except Program.DoesNotExist:
            return DeleteProgram(success=False, message="Program not found.")
        except Exception as e:
            return DeleteProgram(success=False, message=str(e))
    
class Mutation(graphene.ObjectType):
    add_program = AddProgram.Field()
    update_program = UpdateProgram.Field()
    delete_program = DeleteProgram.Field()
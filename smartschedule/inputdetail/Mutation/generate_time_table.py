import graphene
from inputdetail.generate_time_table import generate_timetable

class GenerateTimeTable(graphene.Mutation):
    success = graphene.Boolean()
    message = graphene.String()


def mutate(self,info):
    generate_timetable()
    return GenerateTimeTable(success = True, message="Time table Generated Successiful..")

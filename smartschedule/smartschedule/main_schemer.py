import graphene
from inputdetail.Mutation.allmutation import Mutation
from inputdetail.User.login import UMutation
from smartschedule.inputdetail.Query.Query import Query
class Query(Query, graphene.ObjectType):
    pass

class Mutation(UMutation,Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
import graphene
from inputdetail.schema.allmutation import Mutation
from inputdetail.schema.User.login import UMutation
from inputdetail.schema.Query.Query import Query
# from inputdetail.Objecttype import *


class Query(Query, graphene.ObjectType):
    pass

class Mutation(UMutation,Mutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)
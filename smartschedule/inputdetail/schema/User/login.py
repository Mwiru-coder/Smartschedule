import graphene
import graphql_jwt
from django.contrib.auth import authenticate
from .registration import *
from inputdetail.schema.Objecttype import UserType  # GraphQL user type
from graphql_jwt.mixins import JSONWebTokenMixin

class CustomObtainJSONWebToken(JSONWebTokenMixin, graphene.Mutation):
    class Arguments:
        registration_no = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, registration_no, password):
        user = authenticate(registration_no=registration_no, password=password)
        if user is None:
            raise Exception("Invalid credentials")

        token = cls.get_token(user, info.context)
        return cls(token=token, user=user)
    
    


class UMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    update_user = UpdateUser.Field()
    Logou_tUser = LogoutUser.Field()
    # Auth Mutations
    login = CustomObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

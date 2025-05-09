import graphene
from inputdetail.models import User, Department, Course
from ..Objecttype import UserType


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        registration_no = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        second_name = graphene.String()
        phone_no = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String()
        department_id = graphene.String(required=True)
        course_codes = graphene.List(graphene.ID)  # ManyToMany

    @staticmethod
    def mutate(root, info, registration_no, first_name, last_name, phone_no, email, department_id, course_codes=[], password=None, second_name=None):
        department = Department.objects.get(pk=department_id)
        user = User(
            registration_no=registration_no,
            first_name=first_name,
            last_name=last_name,
            second_name=second_name,
            phone_no=phone_no,
            email=email,
            department_id=department
        )

        if password:
            user.set_password(password)
        else:
            user.set_password(last_name)  # default

        user.save()

        if course_codes:
            courses = Course.objects.filter(pk__in=course_codes)
            user.course_code.set(courses)

        return CreateUser(user=user)




class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        registration_no = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        second_name = graphene.String()
        phone_no = graphene.String()
        email = graphene.String()
        department_id = graphene.Int()
        course_codes = graphene.List(graphene.String)  # List of course codes (if needed)

    def mutate(root, info, registration_no, **kwargs):
        try:
            user = User.objects.get(registration_no=registration_no)

            # Update fields dynamically
            for key, value in kwargs.items():
                if key == "department_id" and value:
                    department = Department.objects.get(id=value)
                    user.department_id = department
                elif key == "course_codes" and value:
                    courses = Course.objects.filter(course_code__in=value)
                    user.course_code.set(courses)
                elif hasattr(user, key):
                    setattr(user, key, value)

            user.save()
            return UpdateUser(user=user, success=True, message="User updated successfully.")
        except User.DoesNotExist:
            return UpdateUser(user=None, success=False, message="User does not exist.")
        except Exception as e:
            return UpdateUser(user=None, success=False, message=str(e))




class DeleteUser(graphene.Mutation):
    success = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        registration_no = graphene.String(required=True)

    def mutate(root, info, registration_no):
        try:
            user = User.objects.get(registration_no=registration_no)
            user.delete()
            return DeleteUser(success=True, message="User deleted successfully.")
        except User.DoesNotExist:
            return DeleteUser(success=False, message="User does not exist.")


class LogoutUser(graphene.Mutation):
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(root,info,):
        return LogoutUser(success = True, message= "Logout succsessful.")




# class BaseMutation(graphene.ObjectType):
#     Create_User = CreateUser.Field()
#     Update_User = UpdateUser.Field()
#     delete_user = DeleteUser.Field()
#     Logou_tUser = LogoutUser.Field()
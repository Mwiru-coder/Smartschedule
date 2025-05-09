from inputdetail.schema.User.login import CustomObtainJSONWebToken
from .course import *
from .program import *
from .Department import *
from .group import *
from .program import *
from .venue import *
from .generate_time_table import GenerateTimeTable


class Mutation(graphene.ObjectType):
    custom_obtain_json_web_token = CustomObtainJSONWebToken.Field()
    add_course = AddCourse.Field()
    update_course = UpdateCourse.Field()
    delete_course = DeleteCourse.Field()
    add_department = AddDepartment.Field()
    update_department = UpdateDepartment.Field()
    delete_department = DeleteDepartment.Field()
    add_group = AddGroup.Field()
    update_group = UpdateGroup.Field()
    delete_group = DeleteGroup.Field()
    add_program = AddProgram.Field()
    update_program = UpdateProgram.Field()
    delete_program = DeleteProgram.Field()
    add_venue = AddVenue.Field()
    update_venue = UpdateVenue.Field()
    delete_venue = DeleteVenue.Field()
    generate_timetable=GenerateTimeTable.Field()
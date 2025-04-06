import graphene
from ..Objecttype import *



class Query(graphene.ObjectType):
    user = graphene.List(UserType)
    user_by_id = graphene.Field(UserType,registration_no = graphene.String)

    course = graphene.List(CourseType)
    course_by_id = graphene.Field(CourseType, course_code = graphene.String)

    program = graphene.List(ProgramType)
    program_by_id = graphene.Field(ProgramType,program_code=graphene.String)

    department = graphene.List(DepartmentType)
    department_by_id = graphene.Field(DepartmentType,department_id=graphene.String)

    venue = graphene.List(VenueType)
    venue_number= graphene.Field(VenueType, venue_number=graphene.String)

    group = graphene.List(GroupType)
    group_by_id = graphene.Field(GroupType,group_id=graphene.String)

    conflict = graphene.List(Conflict)
    conflict_id = graphene.Field(ConflictType,conflict_id=graphene.String)

    Schedule = graphene.List(ScheduleType)


# ...............................................................................
    def resolve_user(root,info, **kwargs):
        return User.objects.all()
    
    def resolve_user_by_id (root,info, registration_no):
        return User.objects.get(pk = registration_no)
    
# ..............................................................................

    def resolve_course(root,info,**kwargs):
        return Course.objects.all()
    
    def resolve_course_by_id(root,info,course_code):
        return Course.objects.get(pk = course_code)
    
# .......................................................................................

    def resolve_program(root,info):
        return Program.objects.all()
    
    def resolve_program_by_id(root,info,program_code):
        return Program.objects.get(pk = program_code)
# ..........................................................................................


    def resolve_department(root,info):
        return Department.objects.all()
    
    def resolve_department_by_id(root,info,department_id):
        return Department.objects.get(pk = department_id)
    
# ..............................................................................................

    def resolve_venue(root,infp):
        return Venue.objects.all()
    
    def resolve_venue_by_id(root,info, venue_number):
        return Venue.objects.get(pk=venue_number)
# ....................................................................................................

    def resolve_group(root,info, **kwargs):
        return Group.objects.all()
    
    def resolve_group_by_id(root,info, group_id):
        return Group.objects.get(pk = group_id)

# .......................................................................................................

    def resolve_conflict(root,info,**kwargs):
        return Group.objects.all()
    
    def resolve_conflict_by_id(root,info,confilict_id):
        return Group.objects.get(pk = confilict_id)
    
# ...................................................................................................

    def resolve_schedule(root,info, **kwargs):
        return Schedule.objects.all().order_by('day','start_time')
    
    
    
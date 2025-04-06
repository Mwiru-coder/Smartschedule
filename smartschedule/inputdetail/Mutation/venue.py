import graphene
from ..models import Venue
from ..Objecttype import VenueType

class AddVenue(graphene.Mutation):
    class Arguments:
        venue_name = graphene.String(required=True)
        venue_number = graphene.String(required=True)
        capacity = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, venue_name, venue_number, capacity):
        try:
            new_venue = Venue(
                venue_name=venue_name,
                venue_number=venue_number,
                capacity=capacity,
            )
            new_venue.save()
            return AddVenue(success=True, message="Venue added successfully.")
        except Exception as error:
            return AddVenue(success=False, message=str(error))  
    
class UpdateVenue(graphene.Mutation):
    class Arguments:
        venue_name = graphene.String(required=True)
        venue_number = graphene.String(required=True)
        capacity = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, venue_name, venue_number, capacity):
        try:
            venue = Venue.objects.get(venue_number=venue_number)
            venue.venue_name = venue_name
            venue.capacity = capacity
            venue.save()
            return UpdateVenue(success=True, message="Venue updated successfully.")
        except Venue.DoesNotExist:
            return UpdateVenue(success=False, message="Venue not found.")
        except Exception as error:
            return UpdateVenue(success=False, message=str(error))
        
    
class DeleteVenue(graphene.Mutation):
    class Arguments:
        venue_number = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, venue_number):
        try:
            venue = Venue.objects.get(venue_number=venue_number)
            venue.delete()
            return DeleteVenue(success=True, message="Venue deleted successfully.")
        except Venue.DoesNotExist:
            return DeleteVenue(success=False, message="Venue not found.")
        except Exception as error:
            return DeleteVenue(success=False, message=str(error))
        
    
# class Mutation(graphene.ObjectType):
#     add_venue = AddVenue.Field()
#     update_venue = UpdateVenue.Field()
#     delete_venue = DeleteVenue.Field()
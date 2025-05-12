import graphene
from ..models import Venue  # Make sure this is the correct path to your Venue model


class AddVenue(graphene.Mutation):
    class Arguments:
        venue_name = graphene.String(required=True)
        venue_number = graphene.String(required=True)
        capacity = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, venue_name, venue_number, capacity):
        if Venue.objects.filter(venue_number=venue_number).exists():
            return AddVenue(success=False, message="Venue with this number already exists.")
        if Venue.objects.filter(venue_name=venue_name).exists():
            return AddVenue(success=False, message="Venue with this name already exists.")
        if capacity <= 0:
            return AddVenue(success=False, message="Capacity must be a positive integer.")
        if not isinstance(venue_name, str) or not isinstance(venue_number, str):
            return AddVenue(success=False, message="Venue name and number must be strings.")
        if not isinstance(capacity, int):
            return AddVenue(success=False, message="Capacity must be an integer.")

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
        except Venue.DoesNotExist:
            return UpdateVenue(success=False, message="Venue not found.")
        
        if capacity <= 0:
            return UpdateVenue(success=False, message="Capacity must be a positive integer.")
        if not isinstance(venue_name, str) or not isinstance(venue_number, str):
            return UpdateVenue(success=False, message="Venue name and number must be strings.")

        venue.venue_name = venue_name
        venue.capacity = capacity
        venue.save()
        return UpdateVenue(success=True, message="Venue updated successfully.")


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
        
    
class Mutation(graphene.ObjectType):
    add_venue = AddVenue.Field()
    update_venue = UpdateVenue.Field()
    delete_venue = DeleteVenue.Field()

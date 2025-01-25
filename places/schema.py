import graphene
from graphene_django.types import DjangoObjectType
from places.models import Place
from users.models import User
from graphene import ObjectType

class PlaceType(DjangoObjectType):
    class Meta:
        model = Place

class Query(ObjectType):
    places_by_user = graphene.List(PlaceType, username=graphene.String(required=True))

    def resolve_places_by_user(self, info, username):
        try:
            user = User.objects.get(username=username)
            places = Place.objects.filter(saved_by=user)
            return places
        except User.DoesNotExist:
            return []

schema = graphene.Schema(query=Query)
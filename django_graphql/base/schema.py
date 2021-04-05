import graphene
from graphene_django import DjangoObjectType

from django_graphql.base.models import SimpleSingle


class SimpleSingleType(DjangoObjectType):
    class Meta:
        model = SimpleSingle
        fields = ("id", "string_field", "bool_field", "int_field", "float_field")


class Query(graphene.ObjectType):
    all_simple_single_type = graphene.List(SimpleSingleType)

    def resolve_all_simple_single_type(root, info):
        return SimpleSingle.objects.all()


schema = graphene.Schema(query=Query)

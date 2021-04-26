import graphene
from graphene_django import DjangoObjectType

from django_graphql.base.models import SimpleSingle


class SimpleSingleType(DjangoObjectType):
    class Meta:
        model = SimpleSingle
        fields = ("id", "string_field", "bool_field", "int_field", "float_field")


class Query(graphene.ObjectType):
    all_simple_single = graphene.List(SimpleSingleType)
    simple_single = graphene.Field(SimpleSingleType, id=graphene.Int())

    def resolve_all_simple_single(root, info):
        return SimpleSingle.objects.all()

    def resolve_simple_single(root, info, id):
        return SimpleSingle.objects.get(pk=id)


class SimpleSingleMutation(graphene.Mutation):
    class Arguments:
        string_field = graphene.String(required=True)
        bool_field = graphene.Boolean(required=True)
        int_field = graphene.Int(required=True)
        float_field = graphene.Float(required=True)

    simple_single = graphene.Field(SimpleSingleType)

    @classmethod
    def mutate(cls, root, info, string_field, bool_field, int_field, float_field):
        simple_single = SimpleSingle(string_field=string_field,
                                    bool_field=bool_field,
                                    int_field=int_field,
                                    float_field=float_field)
        simple_single.save()
        return SimpleSingleMutation(simple_single=simple_single)


class Mutation(graphene.ObjectType):
    update_simple_single = SimpleSingleMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

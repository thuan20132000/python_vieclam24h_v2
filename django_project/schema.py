import graphene
from graphene_django import DjangoObjectType

from realestate.models import Category,Realestate




class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")


class RealestateType(DjangoObjectType):
    class Meta:
        model = Realestate
        fields = ("id","address","province","district")


class Query(graphene.ObjectType):
    all_category = graphene.List(CategoryType)
    category_by_name = graphene.Field(CategoryType,name=graphene.String(required=True))

    def resolve_all_category(root,info):
        return Category.objects.select_related("adminrealestatecategory").all()
    

schema = graphene.Schema(query=Query)


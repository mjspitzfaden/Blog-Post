from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from blog.models import Publication, Post, Categories, Search
class PublicationNode(DjangoObjectType):
  class Meta:
    model = Publication
    only_fields = ('name', 'slug')
    filter_fields = ['slug']
    interfaces = (relay.Node, )
class PostNode(DjangoObjectType):
  class Meta:
    model = Post
    only_fields = ('title', 'body', 'created', 'blog')
    filter_fields = {
      'title': ['exact', 'icontains', 'istartswith'],
    }
    interfaces = (relay.Node, )
class CategoriesNode(DjangoObjectType):
  class Meta:
    model = Categories
    only_fields = ('categories')
    filter_fields = {
      'title': ['exact', 'icontains', 'istartswith'],
    }
    interfaces = (relay.Node, )
class SearchNode(DjangoObjectType):
  class Meta:
    model = Search
    only_fields = ('search')
    filter_fields = {
      'title': ['exact', 'icontains', 'istartswith'],
    }
    interfaces = (relay.Node, )

class Query(ObjectType):
  all_pubs = DjangoFilterConnectionField(PublicationNode)
  all_posts = DjangoFilterConnectionField(PostNode)

schema = Schema(query=Query)

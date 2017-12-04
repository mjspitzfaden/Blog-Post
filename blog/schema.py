from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from graphene_django.filter import DjangoFilterConnectionField
from blog.models import Publication, Post, Categories, Search
from graphene_django.rest_framework.mutation \
    import SerializerMutation
from blog.serializers import PostSerializer, PublicationSerializer

class AddPub (SerializerMutation):
  # perform_mutate needed?
  class Meta:
    serializer_class = PublicationSerializer
class AddPost (SerializerMutation):
  # perform_mutate needed?
  class Meta:
    serializer_class = PostSerializer
class Mutation (ObjectType):
  add_post = AddPost.Field()
  add_pub = AddPub.Field()

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

  def resolve_all_posts (self, info):
    if not info.context.user.is_authenticated():
      return Post.objects.none()
    else:
      return Post.objects.filter(author=info.context.user)

from django.contrib.auth.mixins import LoginRequiredMixin
from jwt_auth.mixins import JSONWebTokenAuthMixin
from graphene_django.views import GraphQLView

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
  pass

write_schema = Schema(query=Query, mutation=Mutation)
read_schema = Schema(query=Query)

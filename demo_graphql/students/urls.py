from django.urls import path
from graphene_django.views import GraphQLView
from .schema.student import student_schema


urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=student_schema)),
]

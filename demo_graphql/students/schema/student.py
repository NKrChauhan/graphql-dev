import graphene
from graphene_django import DjangoObjectType
from ..models import Student


class StudentObjectType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("name", "marks", "date_of_admission", "grade")

class Query(graphene.ObjectType):

    all_students = graphene.List(StudentObjectType)


    def resolve_all_students(root, info):
        return Student.objects.all()

student_schema = graphene.Schema(query=Query)

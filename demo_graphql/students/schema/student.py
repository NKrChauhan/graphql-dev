import graphene
from graphene_django import DjangoObjectType
from ..models import Student


class StudentObjectType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("name", "marks", "date_of_admission", "grade")

class Query(graphene.ObjectType):
    all_students = graphene.List(StudentObjectType, grade=graphene.String(required=False), limit=graphene.Int(required=False))


    def resolve_all_students(root, info, grade=None, limit=None):
        api_filter = {'grade': grade} if grade else {}
        if limit:
            return Student.objects.filter(**api_filter).order_by('-date_of_admission')[:limit]
        return Student.objects.filter(**api_filter)
      

class StudentMutationModel(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        grade = graphene.String(required=True)
        marks = graphene.Int(required=False)

    student = graphene.Field(StudentObjectType)

    def mutate(self, info, name, grade, **kwargs):
        student = Student.objects.create(name=name, grade=grade, **kwargs)
        return StudentMutationModel(student=student)

class Mutation(graphene.ObjectType):
    create_student_entry = StudentMutationModel.Field()


student_schema = graphene.Schema(query=Query, mutation=Mutation)

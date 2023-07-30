import graphene
from graphene_django import DjangoObjectType
from ..models import Student


class StudentObjectType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("name", "marks", "date_of_admission", "grade")


class StudentCreationMutationModel(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        grade = graphene.String(required=True)
        marks = graphene.Int(required=False)

    student = graphene.Field(StudentObjectType)

    def mutate(self, info, name, grade, **kwargs):
        student = Student.objects.create(name=name, grade=grade, **kwargs)
        return StudentCreationMutationModel(student=student)

class StudentUpdateMutationModel(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        marks = graphene.Int()
        grade = graphene.String()

    student = graphene.Field(StudentObjectType)

    def mutate(self, info, id, **kwargs):
        try:
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            raise Exception("Student with the provided ID does not exist.")

        for key, value in kwargs.items():
            setattr(student, key, value)

        student.save()
        return StudentUpdateMutationModel(student=student)
    

class StudentDeleteMutationModel(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        marks = graphene.Int()
        grade = graphene.String()

    student = graphene.Field(StudentObjectType)

    def mutate(self, info, id, **kwargs):
        try:
            student = Student.objects.get(pk=id, **kwargs)
        except Student.DoesNotExist:
            raise Exception("Student with the provided ID does not exist.")

        student.delete()
        return StudentDeleteMutationModel(student=student)


class Mutation(graphene.ObjectType):
    create_student_entry = StudentCreationMutationModel.Field()
    update_student_entry = StudentUpdateMutationModel.Field()
    delete_student_entry = StudentDeleteMutationModel.Field()


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentObjectType, grade=graphene.String(required=False), limit=graphene.Int(required=False))


    def resolve_all_students(root, info, grade=None, limit=None):
        api_filter = {'grade': grade} if grade else {}
        if limit:
            return Student.objects.filter(**api_filter).order_by('-date_of_admission')[:limit]
        return Student.objects.filter(**api_filter)
      

student_schema = graphene.Schema(query=Query, mutation=Mutation)

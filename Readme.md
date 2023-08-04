# Documentation

This Django project consists of 1 app - `students` performing CRUD operation using GraphQL API

## Requirements

To run this project, you will need to have the following installed on your system:

- Python 3.x
- Django 3.x
- Django Rest Framework (DRF) 3.x

## Installation

1. Clone the repository: `git clone https://github.com/NKrChauhan/graphql-dev.git`.
2. Install the project requirements: `pip install -r requirements.txt`.
3. Run database migrations: `python manage.py migrate`.
4. Run the `python manage.py runserver`

## Usage

Request the endpoint to filter all students based on grade or use it without a filter.
endpoint: `http://127.0.0.1:8000/students/graphql/`
write the query.

#### Request query with Screenshots for reference:

 Read query:
```
query{
  allStudents(grade: "sp", limit: 2){
    name
    dateOfAdmission
  }
}
args:
- grade - filter based on grade (not required field)
- limit - limit on number of records (not required field)
```
Mutation to create a student entry
```
mutation {
  createStudentEntry (name: "yami_1", marks:25, grade: "2") {
    student{
      name
      marks
      dateOfAdmission
      grade
    }
  }
}
args:
- grade - required field
- marks - not required field
- name - required filed 
```
Mutation to update student using id with other parameters to update
```
mutation{
  updateStudentEntry(id:1, name: "greg"){
    student{
      grade
      dateOfAdmission
      name
    }
  }
}
args:
- id - required filed 
- grade - required field
- marks - not required field
- name - required filed 
```
Mutation to delete student using id and other filters
```
mutation{
  deleteStudentEntry(id:1, name: "some"){
    student{
      grade
      dateOfAdmission
      name
    }
  }
}
args:
- id - required filed 
- grade - required field
- marks - not required field
- name - required filed 
```
> Read Query
  ![Screenshot 2023-07-30 at 8 21 49 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/c4097512-58ec-4f44-b51f-9db0d40e32a3)

> Delete Mutation
  ![Screenshot 2023-07-30 at 11 21 03 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/f86d346c-4476-4e2d-aad7-f5bf906b5fc0)

> Read Query
  ![Screenshot 2023-07-30 at 10 17 33 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/ef4ec314-9568-4c3a-901e-5121141d2a9d)

> Create Mutation
  ![Screenshot 2023-07-30 at 10 35 24 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/c9b7fd77-9ef2-4cad-bef2-f36035f82f7f)

> Update Mutation
  ![Screenshot 2023-07-30 at 11 04 38 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/061c5588-8d91-49b4-b5e1-0637a46e2798)

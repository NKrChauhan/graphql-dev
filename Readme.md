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
  ![Screenshot 2023-07-30 at 8 21 49 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/c3dea994-6938-4694-87e6-6fc5dfa07d6e) 

> Delete Mutation
  ![Screenshot 2023-07-30 at 11 21 03 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/7c4150d6-d921-42ce-9bc0-999eb8fcada7)

> Read Query
  ![Screenshot 2023-07-30 at 10 18 13 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/e1b2188c-0a40-476b-a59b-e34e5705c69f)

> Create Mutation
  ![Screenshot 2023-07-30 at 10 35 24 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/bd0a6f9f-915f-4e6a-9854-6a6a417a17cc)

> Update Mutation
  ![Screenshot 2023-07-30 at 11 04 38 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/8001f903-38f4-49de-8757-01278ac2a0ea)

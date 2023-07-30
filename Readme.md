# Documentation

This Django project consists of 1 app - `students`

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
writhe the query.

#### Screenshots for reference:

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
Mutation Query to create a student entry
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
![Screenshot 2023-07-30 at 10 35 24 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/bd0a6f9f-915f-4e6a-9854-6a6a417a17cc)

![Screenshot 2023-07-30 at 8 21 49 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/c3dea994-6938-4694-87e6-6fc5dfa07d6e)

![Screenshot 2023-07-30 at 10 18 13 PM](https://github.com/NKrChauhan/graphql-dev/assets/40715943/e1b2188c-0a40-476b-a59b-e34e5705c69f)

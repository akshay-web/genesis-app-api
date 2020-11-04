# genesis-app-api
Project management app api source code

Problem:
Setup a project using Django Rest Framework and Django Rest Auth, that has users and projects. 
A user must be authorized in order to view or make any changes to the database. Projects have the following fields - title, description, status (Active, On Hold, Completed), start date, end date. 
Any number of users can be assigned to projects. Projects should be able to be filtered by any number of params (ex. title, assigned users, etc.). 
If more than one param is input, all params should be accounted for when filtering. The filtering functionality should also accommodate a search term that should take into account all fields of a project, including assigned users.
Project and Users should be serialized and returned as JSON in a list format. 
When a single project is retrieved it should include full serialization of associated users.

Solution:

The project implements above features using djangorestframework and django-rest-auth[with_social] (with social is used to add registration functionality)
Required packages can be installed using requirements.txt. Alternately, we can run below commands:
pip install django
pip install djangorestframework
pip install django-rest-auth[with_social]

To access the api base url is projects/

Filter usage examples:
http://127.0.0.1:8000/projects/?title=chatbot
http://127.0.0.1:8000/projects/?description=python
http://127.0.0.1:8000/projects/?status=Active
http://127.0.0.1:8000/projects/?users=John
http://127.0.0.1:8000/projects/?end_date=2021-12-31
http://127.0.0.1:8000/projects/?start_date=2020-01-01
http://127.0.0.1:8000/projects/?end_date=2021-12-31&status=Active [Combination of filters]
http://127.0.0.1:8000/projects/?search=completed  [Search filter]

Assumption:
All users can get all projects by default if they have view permissions.
If users are required to access only their assigned projects, the last line in views.py can be changed to:
return queryset.filter(users=self.request.user)

Things to note:
1. Superusers will be able to add a new project
2. If a user doesn't have view permissions, it will not be able to get list of projects
3. Unauthenticated users will not be able to perform any operation
4. Registration url: [Email is not required]
http://127.0.0.1:8000/rest-auth/registration/
5. Login url:
http://127.0.0.1:8000/rest-auth/login/
6. Logout url:
http://127.0.0.1:8000/rest-auth/logout/




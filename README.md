# Books API
Starting from the traditional Django, then add in Django REST framework, we will create API having users, permissions, and allow for full CRUD (Create-Read-Update-Delete) functionality. Moreover viewsets, routers, and documentation.

### Permissions
I have used Custom Permissions to allow particular user to EDIT and DELETE his own data, while allowing him to READ the rest. Admin has CRUD access to all users' data

### User Authentication
I have implemented Token Authentication. Using Django REST Auth, I have added Login,Logout and Password Rest endpoints. For User Registration, I have used Django Allauth

### Viewsets and Routers
To make the code more concise, I have implemented viewssets and routers. It comes with the trade off of readability.

### Schemas and Documentation
At the end, I have added Schemas using Core API and and Documentation using built in rest framework feature.

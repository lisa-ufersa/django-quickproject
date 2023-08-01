### Welcom to LISA DRF Quick Project!

Welcome to our Quick Hands-on Django Rest Framework Project! In this interactive learning experience, you will dive into the world of building powerful Web APIs with Django Rest Framework (DRF). Whether you are new to Django or already familiar with it, this project will provide you with a practical, step-by-step approach to create RESTful APIs in no time.

Throughout this hands-on journey, you will explore essential DRF components like serializers, views, authentication, and permissions, among others. You will get hands-on with writing unit tests using pytest to ensure the reliability of your API endpoints. By the end of this project, you will have a solid understanding of how DRF works and the confidence to build robust and efficient Web APIs with Django.

Let's embark on this exciting learning adventure together, where you'll gain valuable skills that will be beneficial for your future projects and development endeavors. Let's get started! Happy coding!

#### Django Rest Framework (DRF)

Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Python using the Django web framework. It provides a comprehensive set of tools and features that make it easier for developers to create robust and efficient RESTful APIs.

Some key features of Django Rest Framework include:

    Serializers: DRF provides serializers to convert complex data, such as Django models, querysets, or Python objects, into JSON or XML for API responses. They also handle deserialization, allowing data to be converted back to native Python data types for processing.

    Viewsets and Views: DRF offers powerful view classes, such as Viewsets and Views, which handle the logic for processing HTTP methods like GET, POST, PUT, PATCH, and DELETE for different API endpoints.

    Authentication and Permissions: DRF includes various authentication methods like Token Authentication, Basic Authentication, and JSON Web Tokens (JWT) to secure APIs. It also supports fine-grained permissions to control access to resources.

    Pagination: DRF allows easy configuration of pagination for API responses, enabling the handling of large datasets efficiently.

    Filtering, Searching, and Ordering: DRF provides filter backends to facilitate data filtering, searching, and ordering of API results, enhancing the API's usability.

Overall, Django Rest Framework is widely adopted in the Python and Django community due to its ease of use, extensive documentation, and versatility in building high-quality and scalable Web APIs. It provides a solid foundation for developers to create RESTful APIs with minimal boilerplate code, allowing them to focus on delivering functional and feature-rich applications.

#### Quick Install

This guide aims to jump start the project settings and bring a fast hands-on DRF Project. However, to enable and run the project, some commands are still required.

- Step 1 - Create a virtual python environment to install all required dependencies:

```python -m venv venv```

- Step 2 - Activate the virtual python environment:

```. venv/bin/activate```

- Step 3 - Install all dependencies:

```pip install -r requirements.txt```

- Step 4 - Run internal server and fun! ;)

```python manage.py runserver```

#### DRF Architecture

The architecture of Django Rest Framework (DRF) is built on top of the well-established architecture of Django, which is a high-level Python web framework. DRF extends Django's capabilities to provide a specialized architecture for building Web APIs (Application Programming Interfaces) following the principles of Representational State Transfer (REST).

Here's a brief description of the key components of the DRF architecture:

    1. Serializers: Handles data conversion between complex data types and API responses.

    2. Views and Viewsets: Manages API request processing and response generation.

    3. URL Routing: Maps URLs to the appropriate API views or viewsets.

    4. Authentication and Permissions: Ensures API security with various authentication methods and fine-grained access control.

    5. Pagination: Efficiently handles large datasets by configuring API response pagination.

    6. Content Negotiation: Responds with different content types based on client requests.

    7; Filtering, Searching, and Ordering: Enables data filtering, searching, and ordering for API results.

    8. API Versioning: Supports API changes while maintaining backward compatibility for older clients.

#### Directory Strucutre

The directory structure of Django Rest Framework (DRF) is similar to the directory structure of a standard Django project. However, DRF introduces some specific directories and files that are essential for building Web APIs. Here's a brief description of the main directories you would find in a typical DRF project:

    Project Root Directory:
        This is the top-level directory of the DRF project.
        Contains the main project configuration file, typically named settings.py, where you define project-wide settings.
        Also includes other configuration files like urls.py, which defines the URL patterns for the entire project.

    App Directories:
        DRF follows Django's app-based architecture, where each app represents a specific functionality or component of the project.
        Each app typically contains its own models.py, views.py, and serializers.py files.
        The models.py file defines the data models for the app.
        The views.py file contains the views and viewsets for handling API requests and responses.
        The serializers.py file defines the serializers for converting data between complex data types and API responses.
    
    Example: 

project_root/
|-- django_quickproject/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|
|-- users/
|   |-- api/
|       |-- views.py
|       |-- serializers.py
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- .gitignore
|-- db.sqlite3 (local database with SQLite)
|-- LICENSE
|-- manage.py
|-- README.md (This file!)
|-- requirements.txt  (optional)

#### Django Models (ORM)

Django Rest Framework (DRF) uses Django's powerful Object-Relational Mapping (ORM) system to interact with databases and manage data persistence in Web APIs. The DRF ORM builds upon Django's ORM, allowing developers to work with API resources as Python objects and easily perform CRUD (Create, Retrieve, Update, Delete) operations on the underlying database. Through the use of Django models, developers can define the data structure of their API resources, including fields, relationships, and constraints. The ORM abstracts the complexities of SQL queries and database interactions, making it easier to work with data and eliminating the need for writing raw SQL queries. Additionally, the DRF ORM supports various database backends, enabling developers to switch between databases seamlessly, providing flexibility and scalability in building APIs. Overall, the DRF ORM simplifies data management and database operations, allowing developers to focus on creating robust and efficient Web APIs with Django Rest Framework.

Example:

```
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

#### DRF Serializers

Django Rest Framework (DRF) serializers play a crucial role in facilitating data conversion between complex Python data types and API representations, such as JSON or XML. Acting as a bridge between Django models or Python objects and API views, serializers allow developers to effortlessly transform complex data into a format that can be easily rendered into standardized responses. The serializers also handle the reverse process of deserialization, enabling incoming data from API requests to be converted into native Python data types for processing. DRF serializers offer a flexible and powerful way to validate data, customize output, and handle relationships between different API resources. With features like nested serialization, field-level validation, and support for complex data structures, DRF serializers streamline the API development process and empower developers to build robust and feature-rich Web APIs with ease.

Example:

```
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
```

#### DRF Views and Class-Based Views

Django Rest Framework (DRF) provides two main approaches for handling API requests and responses: function-based views and class-based views. Class-based views are a more sophisticated and preferred method in DRF due to their modularity and code reusability. They allow developers to organize API logic into separate classes, each representing a specific HTTP method (e.g., GET, POST, PUT, DELETE). Class-based views make it easy to override specific methods, customize behavior, and handle different authentication and permission requirements for each HTTP method. Moreover, DRF also offers specialized class-based views called Viewsets, which further simplify API development by combining common views for a model into a single class. This promotes a cleaner, more structured codebase and fosters efficient API development, making Django Rest Framework an ideal choice for building powerful and maintainable Web APIs.

Function-based View Example:

```
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list_create_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
```

Class-based View Example:

```
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

#### DRF Routing

Django Rest Framework (DRF) routing is an essential component that maps URLs to the appropriate views or viewsets in a Web API. DRF leverages Django's URL patterns to define the API endpoints and associate them with the corresponding views or viewsets. The routing mechanism allows developers to organize and structure API endpoints logically, making it easy to handle different HTTP methods and resource URLs efficiently. By defining the URL patterns in a central location, DRF provides a clear and concise way to define the API's behavior and ensures that incoming API requests are directed to the correct handlers. With DRF routing, developers can create a well-organized and predictable API structure, making it straightforward for clients to interact with the API and access the desired resources with ease.

Example: 

from django.urls import path
from books.views import BookListCreateView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
]


#### Creating Apps

```django-admin startapp new_app_name```

- 1: Add app to INSTALLED_APPS variable at django_quickproject/settings.py;
- 2: Create models at new_app_name/models.py
- 3: Update the database structure to include new models:
        - ```python manage.py makemigrations```
        - ```python manage.py migrate```
- 4: Add the models to admin interface including at new_app_name/admin.py;
- 5: Create a new directory called 'api' at app root directory (new_app_name/api);
- 6: Define serializers to new models at 'new_app_name/api/serializers.py' (create serializers.py file);
- 7: Create API Views at 'new_app_name/api/views.py' (create views.py file);
- 8: Set the routes at 'django_quickproject/urls.py';
        - ```router.register('api/new_view', ViewClass, basename='new_view')```
- 9: Run the server
        - ```python manage.py runserver```
#### Token Authentication

Previosly we set a native token authentication of DRF. Hence, to access token uses the endpoint:
- 'api/token-auth/' send a valid username/password credentials

The admin user credentials are 'admin/adminadmin'. To send a request using JSON use:

{
    "username": "admin",
    "password": "adminadmin"
}

#### Managers and Services

#### Django Tests

Django Rest Framework (DRF) supports unit testing with pytest, a popular testing framework in the Python community. Using pytest, developers can write concise and readable unit tests for their DRF views, serializers, and other components. DRF provides helpful testing utilities and mixins that simplify the process of testing API endpoints and responses. Developers can create test cases by subclassing DRF's APITestCase, which offers various assertion methods for validating API responses, status codes, and other expected behaviors. By combining pytest's powerful features with DRF's testing utilities, developers can efficiently test their Web APIs, ensuring that the API behaves as expected under different scenarios. The flexibility and ease of writing tests with pytest make it an excellent choice for ensuring the reliability and correctness of Django Rest Framework applications.


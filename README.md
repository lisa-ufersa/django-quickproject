### Welcom to LISA DRF Quick Project!

Welcome to our Quick Hands-on Django Rest Framework Project! In this interactive learning experience, you will dive into the world of building powerful Web APIs with Django Rest Framework (DRF). Whether you are new to Django or already familiar with it, this project will provide you with a practical, step-by-step approach to create RESTful APIs in no time.

Throughout this hands-on journey, you will explore essential DRF components like serializers, views, authentication, and permissions, among others. You will get hands-on with writing unit tests using pytest to ensure the reliability of your API endpoints. By the end of this project, you will have a solid understanding of how DRF works and the confidence to build robust and efficient Web APIs with Django.

Let's embark on this exciting learning adventure together, where you'll gain valuable skills that will be beneficial for your future projects and development endeavors. Let's get started! Happy coding!

#### Django Rest Framework (DRF)

Django Rest Framework (DRF) is a powerful and flexible toolkit for building Web APIs in Python using the Django web framework. It provides a comprehensive set of tools and features that make it easier for developers to create robust and efficient RESTful APIs.

Some key features of Django Rest Framework include:

- **Serializers**: DRF provides serializers to convert complex data, such as Django models, querysets, or Python objects, into JSON or XML for API responses. They also handle deserialization, allowing data to be converted back to native Python data types for processing.

- **Viewsets and Views**: DRF offers powerful view classes, such as Viewsets and Views, which handle the logic for processing HTTP methods like GET, POST, PUT, PATCH, and DELETE for different API endpoints.

- **Authentication and Permissions**: DRF includes various authentication methods like Token Authentication, Basic Authentication, and JSON Web Tokens (JWT) to secure APIs. It also supports fine-grained permissions to control access to resources.

- **Pagination**: DRF allows easy configuration of pagination for API responses, enabling the handling of large datasets efficiently.

- **Filtering, Searching, and Ordering**: DRF provides filter backends to facilitate data filtering, searching, and ordering of API results, enhancing the API's usability.

Overall, Django Rest Framework is widely adopted in the Python and Django community due to its ease of use, extensive documentation, and versatility in building high-quality and scalable Web APIs. It provides a solid foundation for developers to create RESTful APIs with minimal boilerplate code, allowing them to focus on delivering functional and feature-rich applications.

#### System Requirements

To build web applications with DRF you will need to include the following requirements on your system:

- Python 3.10 or lattest version;
- Pip 22.0 or lattest version;
- Virtualenv 20.19 or lattest version;

#### Quick Install

This guide aims to jump start the project settings and bring a fast hands-on DRF Project. However, to enable and run the project, some commands are still required.

- **Step 1** - Create a virtual python environment to install all required dependencies:
~~~
    python3 -m venv venv
~~~

- **Step 2** - Activate the virtual python environment:
~~~
    . venv/bin/activate
~~~

- **Step 3** - Install all dependencies:
~~~
    pip install -r requirements.txt
~~~

- **Step 4** - Run internal server and fun! ;)
~~~
    python manage.py runserver
~~~

Stop the server typing Ctrl+C in terminal. 

#### DRF Architecture

The architecture of DRF is built on top of the well-established architecture of Django, which is a high-level Python web framework. DRF extends Django's capabilities to provide a specialized architecture for building Web APIs (Application Programming Interfaces) following the principles of Representational State Transfer (REST).

Here's a brief description of the key components of the DRF architecture:

1. **Serializers**: Handles data conversion between complex data types and API responses.
2. **Views and Viewsets**: Manages API request processing and response generation.
3. **URL Routing**: Maps URLs to the appropriate API views or viewsets.
4. **Authentication and Permissions**: Ensures API security with various authentication methods and fine-grained access control.
5. **Pagination**: Efficiently handles large datasets by configuring API response pagination.
6. **Content Negotiation**: Responds with different content types based on client requests.
7. **Filtering, Searching, and Ordering**: Enables data filtering, searching, and ordering for API results.
8. **API Versioning**: Supports API changes while maintaining backward compatibility for older clients.

#### Directory Structure

The directory structure of DRF is similar to the directory structure of a standard Django project. However, DRF introduces some specific directories and files that are essential for building Web APIs. Here's a brief description of the main directories you would find in a typical DRF project:

**Project Root Directory**:
- This is the top-level directory of the DRF project.
- Contains the main project configuration file, typically named settings.py, where you define project-wide settings.
- Also includes other configuration files like urls.py, which defines the URL patterns for the entire project.

**App Directories**:
- DRF follows Django's app-based architecture, where each app represents a specific functionality or component of the project.
- Each app typically contains its own models.py, views.py, and serializers.py files.
- The models.py file defines the data models for the app.
- The views.py file contains the views and viewsets for handling API requests and responses.
- The serializers.py file defines the serializers for converting data between complex data types and API responses.

Example: 
~~~
project_root/
|-- config/
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
~~~

#### Creating Apps

DRF provides a simple modularization strategy with apps. To create a new app to your project type:
~~~   
   django-admin startapp new_app_name
~~~

Let's start our tutorial project for a Bookstore. We will add an app called **books**.
~~~
   django-admin startapp books
~~~

All apps need be included to INSTALLED_APPS variable at **config/settings.py**.

~~~python
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "users",
    "books", # <--- Our app here
]
~~~
#### Django Models (ORM)

DRF uses Django's powerful Object-Relational Mapping (ORM) system to interact with databases and manage data persistence in Web APIs. The DRF ORM builds upon Django's ORM, allowing developers to work with API resources as Python objects and easily perform CRUD (Create, Retrieve, Update, Delete) operations on the underlying database. Through the use of Django models, developers can define the data structure of their API resources, including fields, relationships, and constraints. The ORM abstracts the complexities of SQL queries and database interactions, making it easier to work with data and eliminating the need for writing raw SQL queries. Additionally, the DRF ORM supports various database backends, enabling developers to switch between databases seamlessly, providing flexibility and scalability in building APIs. Overall, the DRF ORM simplifies data management and database operations, allowing developers to focus on creating robust and efficient Web APIs with Django Rest Framework.


To include new models to our Bookstore, let's add the Book model in **books/models.py** file.

~~~python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
~~~

After create our Book model, we need update the database structure to include new models. 
Type the commands:
~~~
   python manage.py makemigrations
~~~
~~~
   python manage.py migrate
~~~

### Admin Django Interface 

The Admin interface of Django is a powerful and user-friendly tool that comes built-in with the Django web framework. It provides an easy-to-use web-based interface for managing and interacting with the data in the Django application's database. The Admin interface allows developers and administrators to perform CRUD (Create, Retrieve, Update, Delete) operations on model data without writing any custom code. By simply registering models in the Admin interface, developers can access a feature-rich dashboard to view, add, edit, and delete records. The Admin interface can be further customized by defining ModelAdmin classes to control how data is displayed and managed. This makes it an invaluable tool for quickly setting up and managing the backend of Django applications, saving time and effort in development and data administration tasks.

Add follow commands to register the new models in admin site. In **books/admin.py** file add the lines:

~~~python
from django.contrib import admin
from books.models import Book  # <--- import the model

# Register your models here.

admin.site.register(Book)  # <--- register the model
~~~

#### DRF Serializers

The serializers play a crucial role in facilitating data conversion between complex Python data types and API representations, such as JSON or XML. Acting as a bridge between Django models or Python objects and API views, serializers allow developers to effortlessly transform complex data into a format that can be easily rendered into standardized responses. The serializers also handle the reverse process of deserialization, enabling incoming data from API requests to be converted into native Python data types for processing. DRF serializers offer a flexible and powerful way to validate data, customize output, and handle relationships between different API resources. With features like nested serialization, field-level validation, and support for complex data structures, DRF serializers streamline the API development process and empower developers to build robust and feature-rich Web APIs with ease.

To include the serializers let's create a new directory called **api** in **books**, and create a new file **serializers.py**. 
The path to file will be **books/api/serializers.py**. Then, add the following lines:

~~~python
from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
~~~

#### DRF Views and Class-Based Views

DRF provides two main approaches for handling API requests and responses: function-based views and class-based views. Class-based views are a more sophisticated and preferred method in DRF due to their modularity and code reusability. They allow developers to organize API logic into separate classes, each representing a specific HTTP method (e.g., GET, POST, PUT, DELETE). Class-based views make it easy to override specific methods, customize behavior, and handle different authentication and permission requirements for each HTTP method. Moreover, DRF also offers specialized class-based views called Viewsets, which further simplify API development by combining common views for a model into a single class. This promotes a cleaner, more structured codebase and fosters efficient API development, making Django Rest Framework an ideal choice for building powerful and maintainable Web APIs.

Function-based View Example:

~~~python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from books.api.serializers import BookSerializer

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
~~~

Let's include a Class-based View to book list. Create a new file **views.py** in **books/api** directory.
Then include the following lines:

~~~python
from rest_framework.viewsets import ModelViewSet
from books.models import Book
from books.api.serializers import BookSerializer

class BookListCreateView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
~~~

#### DRF Routing

Routing is an essential component that maps URLs to the appropriate views or viewsets in a Web API. DRF leverages Django's URL patterns to define the API endpoints and associate them with the corresponding views or viewsets. The routing mechanism allows developers to organize and structure API endpoints logically, making it easy to handle different HTTP methods and resource URLs efficiently. By defining the URL patterns in a central location, DRF provides a clear and concise way to define the API's behavior and ensures that incoming API requests are directed to the correct handlers. With DRF routing, developers can create a well-organized and predictable API structure, making it straightforward for clients to interact with the API and access the desired resources with ease.

Let's include our view to list books in the **config/urls.py** file to register it in the router. 

~~~python
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from books.api.views import BookListCreateView ### Book View

from users.api.views import UserProfileExampleViewSet

router = SimpleRouter()

router.register("users", UserProfileExampleViewSet, basename="users")
router.register("api/books", BookListCreateView, basename="book-list"), ## <-- Book list view route

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token-auth/", views.obtain_auth_token),
]+router.urls
~~~

That's it! Now run the internal server typing the command:
~~~
   python manage.py runserver
~~~

#### Admin Django Interface

To acesss the admin Django interface, type the following URL in your browser:

    http://localhost:8000/admin/

In the login form type the credentials: 
~~~
login: admin
password: adminadmin
~~~
In the screen look for Books item in the list. Then, on the right top corner click on **ADD BOOK +** button. Will appear a form to include new books on the system. Include many books that you want. Now, let's test our Book List View.

To access the book list type the following URL in browser:

    http://localhost:8000/api/books/

#### Token Authentication

We set a native token authentication of DRF. Hence, to access token use the endpoint:
- **api/token-auth/** send a valid username/password credentials

The admin user credentials are 'admin/adminadmin'. To send a request using JSON use:

~~~json
{
    "username": "admin",
    "password": "adminadmin"
}
~~~

To include new users, create a new endpoint to the User model or add new users using the Admin Django Interface. 
#### Managers and Services

Managers and Services play essential roles in managing data and handling business logic within Web APIs.

**Managers**: DRF Managers are a crucial part of the Django ORM system, providing a convenient way to encapsulate common query logic and database operations for models. By customizing Managers, developers can define specific methods and filters to access data more efficiently, ensuring cleaner and more readable code. Managers allow for code reusability by encapsulating complex queries, making it easier to maintain and modify the data access logic across different parts of the API.

Example:

~~~python
## managers.py
from django.db import models

class PublishedBooksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)
~~~

~~~python
## models.py
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()  # Default Manager
    published_books = PublishedBooksManager()  # Custom Manager
~~~

**Services**: Services in DRF are high-level components designed to handle complex business logic and act as intermediaries between views and models. They help keep views lightweight and focused on handling HTTP requests, while the Services handle the more involved operations. By abstracting business logic into Services, developers promote a modular and maintainable codebase, allowing for better testing and separation of concerns. Services are particularly beneficial when multiple views or viewsets need to perform similar operations, as they enable code reuse and avoid redundancy.

Example:

~~~python
# services.py
from books.models import Book

class BookService:
    @staticmethod
    def calculate_total_price(book_ids):
        total_price = 0
        for book_id in book_ids:
            try:
                book = Book.objects.get(id=book_id)
                total_price += book.price
            except Book.DoesNotExist:
                pass
        return total_price

~~~

Together, Managers and Services enhance the organization and efficiency of a Django Rest Framework project, promoting a clean separation of concerns and facilitating the development of scalable and robust Web APIs.

#### Django Tests

Django Rest Framework (DRF) supports unit testing with pytest, a popular testing framework in the Python community. Using pytest, developers can write concise and readable unit tests for their DRF views, serializers, and other components. DRF provides helpful testing utilities and mixins that simplify the process of testing API endpoints and responses. Developers can create test cases by subclassing DRF's APITestCase, which offers various assertion methods for validating API responses, status codes, and other expected behaviors. By combining pytest's powerful features with DRF's testing utilities, developers can efficiently test their Web APIs, ensuring that the API behaves as expected under different scenarios. The flexibility and ease of writing tests with pytest make it an excellent choice for ensuring the reliability and correctness of Django Rest Framework applications.

Example: 

~~~python
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
from books.api.serializers import BookSerializer

class BookListViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('book-list-create')
        self.book1 = Book.objects.create(title='Book 1', author='Author 1')
        self.book2 = Book.objects.create(title='Book 2', author='Author 2')
        self.expected_data = BookSerializer([self.book1, self.book2], many=True).data

    def test_list_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_data)

~~~

To run the test, use the following command:
~~~
    pytest
~~~

Happy coding and happy learning! For more information, please refer to the official DRF documentation: https://www.django-rest-framework.org/

LISA Team
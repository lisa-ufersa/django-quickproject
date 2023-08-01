## Django Quick Project

### Welcom to LISA DRF Quick Project!

#### Django Rest Framework (DRF)

#### Quick Install

This guide aims to jump start the project settings and bring a fast hands-on Django Project. However, to enable and run the project, some commands are still required.

- Step 1 - Create a virtual python environment to install all required dependencies:

```python -m venv venv```

- Step 2 - Activate the virtual python environment:

```. venv/bin/activate```

- Step 3 - Install all dependencies:

```pip install -r requirements.txt```

- Step 4 - Run internal server and fun! ;)

```python manage.py runserver```

#### DRF Architecture

#### Directory Strucutre

#### Django Models (ORM)

#### DRF Serializers

#### DRF Views and Class-Based Views

#### DRF Routing

#### Creating Apps

```django-admin startapp new_app_name```

- 1: Add app to INSTALLED_APPS variable at django_quickproject/settings.py;
- 2: Create models at new_app_name/models.py
- 3: Update the database structure to include new models:
        - python manage.py makemigrations
        - python manage.py migrate
- 4: Add the models to admin interface including at new_app_name/admin.py;
- 5: Create a new directory called 'api' at app root directory (new_app_name/api);
- 6: Define serializers to new models at 'new_app_name/api/serializers.py' (create serializers.py file);
- 7: Create API Views at 'new_app_name/api/views.py' (create views.py file);
- 8: Set the routes at 'django_quickproject/urls.py';
        - router.register('api/new_view', ViewClass, basename='new_view')
- 9: Run the server
        - python manage.py runserver
#### Token Authentication

Previosly we set a native token authentication of DRF. Hence, to access token uses the endpoint:
- 'api/token-auth/' send a valid username/password credentials

PS.: The admin user is 'admin/adminadmin'

#### Managers and Services

#### Django Tests




## Django Quick Project

### Welcom to LISA Django Quick Project!

This guide aims jump start the project settings and bring a fast hands on Django Project. Then to enable and run the project some comands are still required.

Step 1 - Create a virtual python environment to install all required dependencies:

'''python -m venv venv'''

Step 2 - Activate the virtual python environment:

'''. venv/bin/activate'''

Step 3 - Install all dependencies:

'''pip install -r requirements.txt'''

Step 4 - Migrate the basic database structure to the django project:

'''python manage.py migrate'''

Step 5 - Create a supseruser to manage the project:

'''python manage.py createsuperuser'''

Step 6 - Run internal server and Fun! ;)

'''python manage.py runserver'''
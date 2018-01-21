### Installation

## Future works on the application server
* This project is developed fully in Django
* The sole reason of using django is to enable the fast pace development of the frontend and backend
* The future development might not be used Django, though django can be made for a high performance which uses UWSGI or Gunicorn to unleash the GIL lock of python. Gunicorn also allows multiple thread to be configured which made the python sort of a real multi threading application that can acquires multiple core of the application.

```shell
$ pip install -r requirements.txt

```

```shell
$ python manage.py runserver
```

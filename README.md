# Finding oldest employee from each department in Django

Date: 10/02/2020

### Setup
> `$ pip install -r requirements.txt`  
> `$ python manage.py migrate`  

### Load some test data
  
> `$ python manage.py loaddata core.json`  
or you can create superuser and load from django admin or manage.py shell as well.

### Get value using shell from staticmethod
> `$ python manage.py shell`  
> `$ from core.models import *`  
> `$ Employee.get_oldest_employee_from_department()`

> email at nurulhudarobin@gmail.com for any query

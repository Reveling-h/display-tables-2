
Create project folder
```
django-admin startproject displayTables
```

To begin running server:
```
cd displayTables
python3 manage.py runserver
```
  
  Run to begin migration
```
python3 manage.py migrate
```

Create superuser
```
python3 manage.py createsuperuser
```
Enter a username and password
```
user: Admin
password: admin
```

Create database app
```
python3 manage.py startapp database
```

In settings.py, place in INSTALLED_APPS, include quotes
```
'database,'
```

For following view files to see the code:
in views.py create views

create urls.py file in database/urls.py, add URL patterns

add URL pattern for database in displayTables/urls.py

To use mysql:
in settings.py change DATABASES to
```
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'my_database',
		'USER': 'root',
		'PASSWORD': 'mysqlpass',
		'HOST': '127.0.0.1',
		'PORT': '3306',
		'OPTIONS': {
			'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
		}
	}
}
```

in \_\_init\_\_.py add
```
import pymysql

pymysql.install_as_MySQLdb()
```

Install mysql client
```
python3 -m pip install mysqlclient
```
Log into mysql server using your username and password
```
mysql -u root -p
```
Create database
```
create database my_database;
```
Quit mysql
```
\q
```

create models in models.py

Run this after adding models to model.py to add table to database
```
python3 manage.py makemigrations
```
  Run this after to complete
```
python3 manage.py migrate
```

Create appropriate .html pages for button and to render table

use http://127.0.0.1:8000/admin/ (or whatever port is correct) admin panel to create users for demo

Run app:
```
python3 manage.py runserver
```
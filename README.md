# The Journey To Canada
The journey to canada is a web application created using Django framework with MySQL interfacing for DB. 

## Steps to create the project:
### Step 1 - Install django 
Install the django package from pip
```
python -m pip install django
```

### Step 2 - Create project
Create django project using the following command,
```
django-admin startproject tjtc
```

### Step 3 - Create app
Create an app inside the django project with the command,
```
python manage.py startapp registration
```

## Steps to integrate MySQL
### Step 1 - Install mysqlclient package
Create `mysqlclieny` package for replacing the default sqlite DB with MySQL DB.
```
pip install mysqlclient
```

### Step 2 - Change DATABASES in settings
Open settings.py file inside the project folder. Change the DB properties in `DATABASES`
Remove the existing value in `default` key and add the following:
```
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'user', #name of the database.
        'USER': 'root',
        'PASSWORD': "",
        'HOST': "",
        'PORT': "",
        'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
} 
```

### Step 3 - Create database in phpMyAdmin
Ensure MySQL server is running. Go to [phpMyAdmin](http://localhost/phpmyadmin) portal. Then select `Databases` tab at the top and then create a database with the name given in the settings.py file.

### Step 4 - Create a model
Create a model with the fields required in the models.py of the respective app. 

## Steps to run the application:

### Step 1 - Go to the project directory
Go to the directory which has manage.py file through command line
```
$ D:downloaded repository> cd Django\ Model/tjtc
```

### Step 2 - Run server
Enter the following command to start the server
```
$ D:\Django Model\tjtc> python manage.py runserver
```

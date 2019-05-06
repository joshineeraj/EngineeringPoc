# EngineeringPoc
An application interface to create feature requests. 
A feature request is a request for a feature into the existing piece of software

Application Structure
---------------------
Using 2 applications: 
- **Feature Request (feature_req)**: Main application of the project and contains the datbase models of the application.
- **API (api)**: Contains the API implementation (API endpoints and Serialization) for the application.
Using two applications gives us a more modularised and flexible structure to work with.

Prerequisites
----------------
- Python version >= 3

Installation
-------------
Navigate to application folder and run 
` pip install -r requirements.txt`


Next, open mysql using the root account
---------------------------------------
`
$ sudo mysql`
`
Enter password:
`

Now that we are inside the mysql console with root privileges, we will create a database, a user, and grant all privileges to that user:
```
CREATE USER 'engguser'@'localhost' IDENTIFIED BY 'enggpass';
CREATE DATABASE enggdb charset=utf8;
GRANT ALL PRIVILEGES ON enggdb.* TO 'engguser'@'localhost';
GRANT ALL PRIVILEGES ON testdb.* TO 'engguser'@'localhost';
FLUSH PRIVILEGES;
quit
```

Apply DB migrations:
-------------------
```
  $ python manage.py makemigrations
  $ python manage.py migrate
```
Collect Static files:
---------------------
`python manage.py collectstatic`

Start Gunicorn
----------------
`gunicorn baseproject.wsgi:application --bind=0.0.0.0:9015 --workers=4`

Application Demo URL:
--------------------
 [http://xhr.one](http://xhr.one)




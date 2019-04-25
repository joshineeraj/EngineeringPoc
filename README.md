# EngineeringPoc
EngineeringPoc to Create Feature Requests


#Create a MySQL Database

#Next, open mysql using the root account


$ sudo mysql
Enter password:

Now that we are inside the mysql console with root privileges, we will create a database, a user, and grant all privileges to that user:

CREATE USER 'engguser'@'localhost' IDENTIFIED BY 'enggpass';
CREATE DATABASE enggdb charset=utf8;
GRANT ALL PRIVILEGES ON enggdb.* TO 'engguser'@'localhost';
FLUSH PRIVILEGES;
quit

python manage.py collectstatic
#Start Gunicorn
gunicorn baseproject.wsgi:application --bind=0.0.0.0:9002 --workers=4



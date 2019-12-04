# product-api
A simple CRUD product API with Python + Django + DRF


## Installation

### Create virtualenv
> The project was developed with linux (fedora 31) system. I've used **Python v3.7.5** and **sqlite3 v3.30.0**.

First of all clone the project to your local machine
```bash
[user@machine ~]$ git clone https://github.com/rk4bir/product-api.git
```

Goto product-api directory
```bash
[user@host ~]$ cd product-api/
```

Create virtual environment with `virtualenv`
```bash
[user@host product-api]$ virtualenv -p /usr/bin/python3 env
```

Now activate the environment
```bash
[user@host product-api]$ source env/bin/activate
``` 

Then install the dependencies from *requirements.txt* file
```bash
(env) [user@host product-api]$ python -m pip install -r requirements.txt
```

Sync the database
```bash
(env) [user@host product-api]$ python manage.py migrate
``` 

To add data to the database create a superuser, if you use 
given `products.sqlite3` database then the credentials are -
* username: admin
* password: admin123
```bash
(env) [user@machine product-api]$ python manage.py createsuperuser --username admin
```
This will prompt for email and password. Once the user is created. 

\
Finally start the development server
```bash
[user@host product-api]$ python manage.py runserver
``` 

Now goto: [Dev server](http://127.0.0.1:8000/products/)\
To insert product data visit [Admin panel](http://127.0.0.1:8000/admin/)

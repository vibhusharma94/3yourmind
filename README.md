
**App Setup (Ubuntu)**

1. Dev tools Installations
  * sudo apt-get update
	* sudo apt-get install build-essential python-dev libevent-dev libxml2-dev libmysqlclient-dev python-setuptools python-pip libpq-dev libxslt1-dev
2. Install Git
  * sudo apt-get install git
3. Clone Repository
  * git clone https://github.com/vibhusharma94/3yourmind.git
4. Install PIP and VirtualEnv.
  * sudo apt-get install python-pip
  * sudo apt-get install python-virtualenv
5. Install Mysql
    * sudo apt-get install mysql-server
    * sudo service mysql stop
    * sudo service mysql start
    


====================================================================

**Setup Steps:**


1. Environment Setup:
       * Create a virtual environment
           * virtualenv env
       * Activate virtual environment
           * source env/bin/activate
       * Install the requirements by running the command:
           * pip install -r requirements.txt
               
2. Database Setup:
       * Create a database with the name '3yourmind_db'
           * mysql -u root -p
           * create database 3yourmind_db;
       * Django db setup: 
           * Run `python manage.py makemigrations company`
           * Run `python manage.py migrate`
       * Create SuperUser: 
           * Run `python manage.py createsuperuser`

3. Starting the Django server locally:
       * python manage.py runserver 8000



 Rest API Documentation
-----------------------------

##**User API**

###  **Upload Api upload stl file**
    
  http://127.0.0.1:8000/upload

##### **POST**

*Request*

  #!shell
  curl -X POST \
  http://127.0.0.1:8000/upload/ \
  -H 'content-disposition: attachment; filename=file;' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F file=@tubeSup.stl

*Response*
```
#!json
{
    "results": [
        {
            "volume": 18536.8515625,
            "name": "platinum"
        },
        {
            "volume": 18536.8515625,
            "name": "silver"
        }
    ]
}
```

###  **Upload Api Retrieve suppliers **
    
  http://127.0.0.1:8000/upload/

##### **GET**

*Request*

  #!shell
  curl -X GET \
  'http://127.0.0.1:8000/upload/?name=platinum&volume=345'

*Response*
```
#!json
{
    "results": [
        {
            "company": {
                "name": "3Dream",
                "id": 4
            },
            "material": {
                "name": "Platinum",
                "id": 10
            },
            "unit_price": "3.00",
            "total_price": 1035
        },
        {
            "company": {
                "name": "Shapeways",
                "id": 1
            },
            "material": {
                "name": "Platinum",
                "id": 10
            },
            "unit_price": "6.00",
            "total_price": 2070
        }
    ]
}
```

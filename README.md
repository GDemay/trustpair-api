# REST API with Flask
## Description

This API was developed for Truspair

Technologies: **Python, Flask, sqllite, SQLAlchemy**

It’s a restaurant API where you can create, update and delete a restaurant (identified by its name), and also list restaurants, get a restaurant by name and get a random
restaurant. 

## Build application

Git clone the project: 

```
git clone https://github.com/GDemay/api-trustpair.git
```

Build the image from the Dockerfile in the repository
```
docker build -t apitrustpair:latest .
```

Create a container from the image.

```
docker run -d -p 5000:5000 apitrustpair
```

Now visit http://localhost:5000
```
 * Serving Flask app 'database.config' (lazy loading)
   ...
 * Debug mode: on
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

**If you have problems generating the database, do these different command lines**

```
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
```

More information here:
https://flask-migrate.readthedocs.io/en/latest/

## Test

To test the API calls of this project, I decided to use Pytest.

To test the project:

```
pytest test/test_flask.py 
```
Output:
```
(virtual) gdemay@DESKTOP-DEMAY-G:~/api-trustpair$ pytest test/test_flask.py 
===================================== test session starts =====================================
platform linux -- Python 3.9.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/gdemay/api-trustpair
collected 10 items                                                                            

test/test_flask.py ..........                                                           [100%]

===================================== 10 passed in 0.14s ======================================
(virtual) gdemay@DESKTOP-DEMAY-G:~/api-trustpair$ 
```

### Architecture

This project uses [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) design pattern. 

### Models

Restaurant Model has 3 fields:

* **id** (int): unique id for the restaurant (primary key)
* **name** (string): name of the restaurant
* **description** (string): description of the restaurant

### Routes

* GET ```/restaurants``` get all restaurants
* GET ```/restaurants/random```  get a random restaurant
* GET ```/restaurants/<string:name>``` get a specific restaurant by giving a name
* POST ```/restaurants``` add a restaurant by giving a name and a description
* DELETE ```/restaurants/<string:name>``` delete a restaurant by giving a name
* PUT ```/restaurants/<string:name>``` update a restaurant by giving a name and a description

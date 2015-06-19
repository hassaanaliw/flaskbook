# flaskbook
A Social Website implementation in Flask. This is something I wrote to learn how Flask works and how to integrate commonly used features such as login, registering etc. in Flask. As a result it may come across as feature-bare.

##Features
* Creating Posts
* Deleting Posts
* Liking and Unliking Posts
* Following and Unfollowing Users
* Remember-Me Functionality
* Markdown Support for Posts (Including Images)

##Running Flaskbook

###Starting Locally

First clone FlaskBook locally by running

``` git clone https://github.com/hassaanaliw/flaskbook.git```

cd to the directory containing flaskbook. Before running flaskbook we must create the users.db Database. Run the following commands

``` 
    python
    > from app import db
    > db.create_all()
    > exit()
```

Once the database has been created simply run 

``` python run.py ```

and navigate to [localhost:5000](http://localhost:5000) to see FlaskBook running.

##Structure
This app uses a modular structure and Blueprints to make the code organised. 

```
app
  ├──- user 
  │   └── models.py
  │   └── views.py
  ├── posts 
  │   └── models.py
  │    └── views.py
  ├── templates
  │   └── *various html files*
  ├── static
  │   └── css
  │    └── js
  ├── helpers.py 
  └── __init__.py
run.py
Procfile
requirements.txt
config.py
```
The root directory contains mostly settings. 

The [**config.py**]() contains the configurations for Dev and Production Environments.

The [**Procfile**]() contains instructions for Heroku as to which file it must run.

The [**run.py**]() contains the code that launches the Flask app.


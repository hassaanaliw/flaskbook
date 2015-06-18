# flaskbook
A Social Website implementation in Flask. This is something I wrote to learn how Flask works and how to integrate commonly used features such as login, registering etc. in Flask. As a result it may come across as feature-bare.

##Features
-------------------
* Creating Posts
* Deleting Posts
* Liking and Unliking Posts
* Following and Unfollowing Users
* Remember-Me Functionality
* Markdown Support for Posts (Including Images)

##Structure
--------------
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


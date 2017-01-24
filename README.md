README

My Big Fat Site 

Place of residence: ~/projects/mybigfatsite

My Big Fat Site is a Django web application which will have at least two apps (plugins), a page entitled Pronunciation Training which will house detailed instruction on an English pronunciation training, and my developer blog.

Below will be the exact steps taken to build the application. 

Project Task Completion

1. Create a root directory for the project on my local machine

 $ mkdir mybigfatsite
$ cd mybigfatsite

“””
It is within this directory that I (after activating virtualenv): 
- install django application and app
- install all other dependencies
- run  $ git init
“””

2. Create and activate virtualenv for the project in root directory

$ virtualenv ~/virtualenvs/mybigfatsite_venv

$ . ~/virtualenvs/mybigfatsite_venv/bin/activate

Check to confirm current virtualenv home:

$ echo $VIRTUAL_ENV
/home/jmm/virtualenvs/mybigfatsite_venv

3. Make it usable as a Python package 

$ touch __init__.py


4. Install Django and see where it lives

$ pip install django

Downloading Django-1.10.5-py2.py3-none-any.whl (6.8MB):   # django 1.10.5

$ which django-admin.py			# Command to find django's home in virtualenv

/home/jmm/virtualenvs/mybigfatsite_venv/bin/django-admin.py

5. Create a django project (Application) in root directory

Project (application) name: myBigFatSite

$ django-admin startproject myBigFatSite

What we have in root directory mybigfatsite/ so far:

__init__.py  myBigFatSite  README.md

6. Enter top django project (application) directory, runserver, and create an app (plugin)

$ cd myBigFatSite

$ ls

manage.py  myBigFatSite		# I'll give application (project) name camelCase

$ python manage.py runserver

It works :)

Make an 'app' (aka plugin) which will live beside manage.py

App (plugin) name: pronunciation_training		# I'll give app (plugin) names under_score

$ python manage.py startapp pronunciation_training
$ python manage.py startapp dev_blog

~/mybigfatsite/myBigFatSite$$ ls

db.sqlite3  dev_blog manage.py  myBigFatSite  pronunciation_training

7. a. Create a .gitignore file (which is invisible)

$ touch .gitignore

7. b. Add types of file that should be ignored by Git and not be sent to Github and hence not into production environment.

$ nano .gitignore

mybigfatsite_venv #virtualenv directory
*.DS_Store
*.pyc
__pycache__
*~
db.sqlite3
/static

7. c. Save changes to file with: Ctrl o
   d. Exit with: Ctrl x

8. a. Initiate a git repository in root directory

$ cd .. to root directory

8. b. 

~/mybigfatsite$ git init

9. Add requirements.txt file with freeze which includes a list of all packages in current environment and their respective versions.

$ pip freeze > requirements.txt

10. Create a repository on Github, then send project from l

$ git status

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	.gitignore
	README.md
	__init__.py
	myBigFatSite/
	requirements.txt

$ git add .				Adds all project directories and files except what is in .gitignore

$ git remote add origin https://github.com/miller2082/mybigfatsite.git

$ git push -u origin master

That is it! We are up on Github!

01/24/2017

ADJUSTMENTS TO myBigFatSite/settings.py

added:

TIME_ZONE = 'JP', However, since this did not mesh up with language it threw an error.

STATIC_URL = '/static/'	# This was already there
Added:
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS was empty. 

For deployment to Pythonanywhere it is changed to:
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

Added a second app, dev_blog, but when I run the runserver command only the 
html response for the first app, pronunciation_training, runs on the browser.

























*** TO BE COMPLETED IN PRODUCTION ENVIRONMENT :: PYTHONANYWHERE ***
CREATE AND SET UP A MySQL Database



a. Installation of MySQL and dependencies

$ sudo apt-get install python-dev mysql-server libmysqlclient-dev

$ easy_install -U distribute

$ sudo mysql_install_db		# for database structure

$ sudo mysql_secure_installation	# Security checks

b. Install MySQL into project virtualenv

$ pip install MySQL-python

MySQL-python in /home/jmm/virtualenvs/mybigfatsite_venv/lib/python2.7/site-packages

*** The development SQLite will be used until the project is moved to Pythonanywhere ***















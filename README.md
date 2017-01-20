README

My Big Fat Site 

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

~/mybigfatsite/myBigFatSite$$ ls

db.sqlite3  manage.py  myBigFatSite  pronunciation_training

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
















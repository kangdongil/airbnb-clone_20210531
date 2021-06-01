# 준비하기

- Chrome
- VSCode
  - Extension: Python
- Python
- VEW(VirtualEnvWrapper)
- Git
  - `git init`
  - `git remote origin master ~.git`

# 0.4 Django란,

- a big toy that we have to learn how to use.

- Always read 'Comment(#)' and Documents
  [Doc](https://docs.djangoproject.com/)

# 2.0 Django 설치하기

- `pip install Django==2.2.5`
- `which django-admin` || `django-admin`

# 2.0.1 Django 프로젝트 시작하기

- `django-admin startproject config`
- Open up the 'config' folder to parent folder
- Create .gitignore and put python gitignore
  [Link](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore)

# 2.1 Linter와 Formatter 설치하기

- Set Interpreter
  - turn on virtual environment
    VEW: `workon [virtualenv]`
  - Set Interpreter on python with specific virtualenv
    [Ctrl+Shift+P] `Python: Select Interpreter`
    ex. `Python 3.9.0 64-bit ('django')`
- Install Linter: flake8
  - `pip install flake8`(console)
  - [Ctrl+Shift+P] `Python: Enable Linting`
  - [Ctrl+Shift+P] `Python: Select Linter`
- Install Formatter: black
  - `pip install black`(console)
  - [Ctrl+,] `Python: Formatting Provider` as 'black'

* Linter: help catch error by highlighting before execute code
* Formatter: help code follow the convention

# 2.2 Django 프로젝트 구조 알아보기

- Project
  - A group of applications
- Application
  - A group of functions specific to a part of our project (users, photos, messages)
  - Application should be as small as possible
- Function & Class

- `manage.py`
  - Execute manage.py command
    `python manage.py [command]`
  - `python manage.py runserver`
  - `python manage.py createsuperuser`
  - `python manage.py makemigration`
  - `python manage.py migrate`
- `/config`
  - `urls.py`: Manage Routers
-

- `apps.py`: Configure Application
- `models.py`: Describe the shape of our app's data
- `admin.py`: Configure the Django Admin panel
- `views.py`: Render HTML for EndUser

* `__init__.py`: file give access to python
  - We put it on a file so we can import it from Python
* `db.sqlite3`: Development-use DataBase
* framework vs. library
  - A framework uses your code, you use the library.

# 2.3 Django Server와 Adminpanel

- Run Migration
  `python manage.py makemigration`
  `python manage.py migrate`
- Create SuperUser(adminpanel access-purpose)
  `python manage.py createsuperuser`
- Start Django Server
  `python manage.py runserver`
  `http://127.0.0.1:8000/`
- Django Admin
  `http://127.0.0.1:8000/admin`

* migration: change the shape of the data on the database
  - DB can be handled with SQL Language
  - Django will update DB with migration system
  - `makemigration`: when new type of data added
  - `migrate`: when data added

# 2.6 Django App 만들기

- Create Application
  `django-admin startapp [plural-name]`
  ```
  users, rooms, reviews, conversations, lists, reservations
  ```

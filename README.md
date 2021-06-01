# 준비하기

- Chrome
- VSCode
  - Extension: Python
- Python
- VEW(VirtualEnvWrapper)
- Git
  - `git init`
  - `git remote origin master ~.git`

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

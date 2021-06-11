# 준비하기

- Chrome
- VSCode
- VSCode Extension
  - Python
  - Djaneiro - Django Snippets
  - Jinja
- Python
- VEW(VirtualEnvWrapper)
- Git
  - `git init`
  - `git remote origin master ~.git`

# 0.4 Django란,

- a big toy that we have to learn how to use.

- Always read 'Comment(#)' and Documents
  [Doc](https://docs.djangoproject.com/)

- Import Sequence Convention:
  `Python` >> `Django` >> `Third-Party` >> `Custom`

# 2.0 Django 설치하기 & 실행하기

- Installation
  `pip install Django==2.2.5`
- Check-if-Install
  `which django-admin` || `django-admin`
- Execution
  `python manage.py shell`

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
  - `settings.py`
    TIMEZONE = "Asia/Seoul"
  - `urls.py`: Manage Routers
- `/[App]`
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
  - Migration should be little as possible

# 2.6 Django Application 만들기

- Categorize Application
  - `/config/settings.py`
  - INSTALLED_APPS >> DJANGO_APPS
  - Seperate `INSTALLED_APPS` to `DJANGO_APPS` and `PROJECT_APPS`
    `INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS`
    `PROJECT_APPS = ["~"]`
  - Add `THIRD_PARTY_APPS`
    `THIRD_PARTY_APPS = ["~"]`
- Create Application
  `django-admin startapp [plural-name]`
  ```
  users, rooms, reviews, conversations, lists, reservations
  ```
- Register Application
  - `/config/settings.py`
  - add `[AppsName].apps.[AppsName]config`
    in PROJECT_APPS
- Migrate changes

- Create Model
- Form AdminPanel

* Object Oriented Programming: extend object by inheriting
* CB(ClassBased)
  - Inherit
  - Docstrings
    `""" ~ Definition """`

# 3.0 User App 만들기

- There is already default Django User Application
  profile, status, group, permission
- We need to extend the default one

- `/config/settings.py`
  - add `AUTH_USER_MODEL`
    - AUTH_USER_MODEL = "[AppName].[ModelName]"
      `AUTH_USER_MODEL = "users.User"`
- `/users/models.py`
  - create model `User`
  - inherit `AbstractUser`
    `from django.contrib.auth.models import AbstractUser`
  - create fields
    ```
    avatar(ImageField) / gender(CharFieldChoices) / bio(TextField) /
    birthdate(DateField) / language(CharField) / currency(CharField) / superhost(BooleanField)
    ```
- `/users/admin.py`
  - create admin `CustomUserAdmin`
  - inherit `UserAdmin`
    `from django.contrib.auth.admin import UserAdmin`
  - configure fieldsets by extending default one
    `fieldsets = UserAdmin.fieldset + (~)`

# 3.0.1 Django Model 만들기

- Import Meta Model
  `from core import models as CoreModels`
- Create Model
  - Create class in `models.py`
    ```
    class [ClassName]([Inherit]):
    pass
    ```
  - for most App, inherit 'models.Model'
    `class User(models.Model):`
  - For User App, inherit AbstractUser
    (If you want to inherit default one)
    `from django.contrib.auth.models import AbstractUser`
    `class User(AbstractUser):`
- Create Fields for model
  - `[FieldName] = models.[Field]()`
  - Set `default=""` or `null=True`
    - settings needed to handle existing data, when new column is added
    - `default=""` is add "" when it's empty
    - `null=True` is leaving as empty
  - Set Arg `blank=True` when blank is allowed
    - `default` and `null` is for DB
    - `blank` is for the Admin Form
- Give Functionality on Model
  Model Function is used for entire homepage
  - How to add function
    ```
    def [Title](self, obj):
          ~
          return [Something]
    ```
  - Name Function when displayed
    [FunctionName].short_descriptions = ""
- Give Name to Model's Object(`__str__`)

* model: describe shape of the data
  - when new model or field is added, we need to migrate
* field: help define how the valid data is
  - model is made out of fields
  - django migration will convert field into SQL
* FieldType - Text
  - TextField()
    : Multi-Line Text
  - CharField()
    : One-Line Text, Limited Letter
    max_length=
  - CharField(choices=[Tuple])
    1. Create Constants
       `[ConstantName]="[DBValue]"`
       `GENDER_MALE="male"`
    2. Create Tuple for choices
       ```GENDER_CHOICES=(
         ([Constant], "[Form]"),
         )
       ```
       `(GENDER_MALE, "Male")`
    3. Add Arg in CharField
       `models.CharField(choices=[CHOICES], max_length=~,)`
* FieldType - Numeric
  - IntegerField()
  - DecimalField()
* FieldType - Others
  - BooleanField()
    True || False
  - DateField()
    - Required:
      `null=True`
    - `auto_now=True`
      : get date and time when model saved
    - `auto_now_add=True`
      : get date and time when model first created
  - TimeField()
  - DateTimeField()
  - CountryField()
    - `pip install django-countries`
      [Link](https://github.com/SmileyChris/django-countries)
    - `django_countries` in THIRD_PARTY_APP
    - `from django_countries.fields import CountryField`
    - `[FieldName] = CountryField()`
* FieldType - File
  - ImageField()
    - `pip install pillow`
    - upload_to
      when subfolder for download is needed
  - FileField()

# 3.0.2 Django AdminPanel [만들기

- Form AdminPanel
  - `admin.py`
  - Register model into admin
    - `from . import models`
    - Original Way
    ```
    class [AdminName](admin.ModelAdmin)
    admin.site.register(models.[Model], [AdminName])
    ```
    - Using Decorater(@)
    ```@admin.register(model.[Model])
    class [AdminName](admin.ModelAdmin):
    pass
    ```
- Organize AdminPanel
  - fieldsets
    `fieldsets = ([Title], {[Content]})`,
    `[Content]`: `"[Attribute]": (~)`
    - "fields"
    - "classes"
      - "collapse"
        : allow folding fieldset
- Arrange AdminPanel
  - list_display
    - display what column are you display on adminpanel
    - `list_display = ("~", "~")`
    - add `__str__` if default one is needed
  - list_filter
    - allow filter on right panel
    - `list_filter = ("~", "~")`
  - search_fields
    `search_fields = ("~")`
    - search case Prefix
      - icontain(default): insensitive on case
      - startswith(^)
      - iexact(=)
      - search(@)
  - ordering
    `ordering = ("~")`
    set default ordering
  - raw_id_fields
    when long list of items expected, item can be displayed as id
- Give Functionality on AdminPanel
  Admin Function mostly used only on Admin
  - How to add function
    ```
    def [Title](self, obj):
          ~
          return [Something]
    ```
    - To use managers, use `self` argument
  - Name Function when displayed
    [FunctionName].short_descriptions = ""
  - Display Function
    add in `list_display`
  - Duplicate Function by class meta
  - Enable Boolean Mark
    `[Function].boolean = True`

* fieldsets: A group of fields
* Assign Name to Object
  set model a method `__str__`
  ```def __str__(self):
        return self.name
  ```
  - This name will appear on adminpanel
  - Django AdminPanel, it looks like blue title row
  - fieldsets = ([fieldset]("[FSName]", [content]{"field": ("~","~",)}),)
  - Default Fieldset: [AdminName].fieldsets
  ```
  fieldset = (
      (
        "Custom",
        {
          "fields": (
            "avatar",
            "gender",
            "bio"
          )
        }
      ),
    )
  ```

# 4.0 Abstract Model 만들기

- Create Core App
  - `django-admin startapp core`
  - `core.apps.CoreConfig`
- Add TimeStampedModel and add `class Meta`
  ```class Meta:
    abstract=True
  ```
- Import CoreModel
  `import core.models as CoreModel`

* abstract model: models that doesn't appear in DB
  - models mostly used to extend mode`s

# 4.1 Room App 만들기

- Create model `Room`
  ```
  name / description / country / city / price / address /
  guests / bedrooms / baths / check_in / check_out / instant_book /
  host / room_type
  ```
- Create model `AbstractItem`
  - `class Meta: abstract=True`
  - `name = CharField(~)`
  - Inherit `AbstractItem` for Item Model
  - Display Item Model on adminpanel
    - can register multiple models
  -

# 4.2 Relationship란, (ForeignKey, ManytoMany)

- ForeignKey(Many-To-One): Connect one model to the other
  - `models.ForeignKey([ModelName], on_delete="models.~")`
  - `on_delete`: behavior when referenced object is deleted
    - CASCADE: affect every sub-object
    - PROTECT: forbid deletion until sub-object exist
    - SET_NULL: sub-object becomes orphan
    - SET_DEFAULT: default after deletion
  - gives access to other model's data
    `models.ForeignKey("users.User", ~)`
    `room.host(users).email`
- ManyToMany Relationship
  - `models.ManyToManyField([ModelName])`
  - to improve adminpanel,
    `filter_horizontal = (~)`
-

- String Method(Reference)
  Instead of Import, You can use String("~") to refer model. for model from other app, "[app].[model]"
- `__` Lookup Method
  `[ForeignKey]__[RelatedName]`

# 4.5 Meta Class란,

- abstract=True
- verbose_name
- verbose_name_plural
- ordering=["Field"]
  reverse order for ["-Field"]

* Meta Class

- builtin class in model with some configuration options

# 6.3 Managers, QuerySets이란,

- How to use Manager
  `[Module].objects.~()`

  - objects.all()
    Cautious when DB has huge amount of data
    Make sure it doesn't evaulate on whole range
    Set `offset` and `limit` by adding [~:~]

  - objects.get(~)
  - objects.count()
  - objects.create([field])
  - objects.[ManyToMany].add(~)

* Manager: Help get data from DB
  `[Model].objects`
* QuerySet: List of Object
* QuerySet Method
  - `[QuerySet].filter()`
* `_set`: Allow reverse-acesss to elements when ForeignKey
* related_name: Modify name for `_set`
  - related_name should be same as Model.(Because it's for target)
  - reverse-accessor clashes, `[~]_[models]`
  - related_name can shorten names.

# 7.0 유용한 Python 명령어

- dir([object])
  Return list of name
- vars([object])
  Return `__dict__` for class
- super().~
  Execute code from Parent Class

# 8.3 Django에서 Media 다루기

- Set path for uploaded media files
  - default path is "/"(root)
  - `/config/settings/py`
      <!-- Before Django 2.0 ver -->
    `MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")`
      <!-- After Django 3.1 ver -->
    `MEDIA_ROOT = BASE_DIR / "uploads"`
- .gitignore `/uploads`
- Connect `/uploads` folder to `media/` URL
  - `/config/settings.py`
    `MEDIA_URL = "/media/"`
- Enable `/media` URL only in Development
  - `/config/urls.py`
  - import `settings` and `static`
    `from django.conf import settings`
    `from django.conf.urls.static import static`
  - get access to `/media` if `debug=True`
    ```
    if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
- Enable adding media from where it belongs to
  - add `inline=([Class])` in model
  - create class inherit Inline
    ```
    class PhotoInline(admin.[InlineStyle]):
    model = ~
    ```
- Output Image on AdminPanel
  - return <img /> HTML
    `<img width="50px" src="~" />`
  - get photo url by obj
    `obj.[ImageField].url`
  - mark_safe <HTML>
    `from django.utils.html import mark_safe`
    `mark_safe(<HTML>)`

* MEDIA_URL: URL that handles the media served from `MEDIA_ROOT`
  - must end in a slash(/)
  - start with slash will make url absolute
* Style of Inline
  - TabularInline
  - StackedInline

# 8.7 Save event를 Intercept하기

- save()
  suitable to save in model
  ```
  def save(self, *args, **kwargs):
  <!-- Do Something -->
  super().save(*args, **kwargs)
  <!-- Do Something Else -->
  ```
- save_model()
  save happens from adminpanel
  ```
  def save_model(self, req, obj, form, change):
        print(obj, change, form)
        super().save_model(req, obj, form, change)
  ```

# 9.0 `manage.py` Command 만들기

- Create folders `/management/commands/`
  Create `__init__.py` in each folders
- Create `seed_[something].py` in `/command`
- Import `BaseCommand`
  `from django.core.management.base import BaseCommand`
- Create class `Command` inherit `BaseCommand`
  `class Command(BaseCommand):`
- Code `Command` class
  - help = "~"
  - To add Argument, (optional)
    ```
    def add_arguments(self, parser):
    parser.add_argument(
      "--[ArgName]", help="~"
    )
    ```
  - To execute code
    ```
    def handle(self, *arg, **options):
    ~
    self.stdout.write(self.style.SUCCESS("~"))
    ```

# 9.1 Django Seed로 데이터 Seed하기

- Install `django_seed`
  `pip install django_seed`
- Add `django_seed` in `THIRD_PARTY_APPS`
  `/config/settings.py`
- Import Seeder and Module
  ` from django_seed import Seed`
  `from [apps].models import [Module]`
- Add "number" argument
  ```
  parser.add_argument(
    "--number", default=1, type=int, help="~"
  )
  ```
- Use Seeder on `handle` method
  - Start Seeder
    `seeder = Seed.seeder()`
  - Add seeder_entity
    `seeder.add_entity([Module], number, {[Detail]})`
    - {[Detail]}
      `{"[field]": ~}`
- Execute Seeder
  `seeder.execute()`
- Customizing Seeder with `lambda x`
  - seeder.execute() return pks
    - set variable `pk_list`
      `pk_list = seeder.execute()`
    - flatten it
      `from django.contrib.admin.utils import flatten`
      `pk_list = flatten(list(pk_list.values()))`
    - use it on your own

* faker: library for fake stuff
  [Link](https://faker.readthedocs.io/en/master/providers/faker.providers.address.html)
* Case of Random Example:
  `import random`
  - random choices
    - import QuerySets
      `[QuerySet] = [Module].objects.all()`
    - random.choice
      `"[field]": lambda x: random.choice([QuerySet])`
  - random number
    `[field]: lambda x: random.randint([from], [to])`
* Case of Seeder_Faker Example
  `"name": lambda x: seeder.faker.address()`
  `"name": lambda x: seeder.faker.sentence()`

# 10.0 Django Url과 View 알아보기

- Syntax of URL
  path("[URL]", [VIEW])

* url: way how direct request
* view: function how reply to request
  - when accessd View with URL, create `HttpRequest`
  - When `HttpRequest` occured, `HttpResponse` is mandatory

# 10.0.1 Django URL 관리하기

- `/config/url.py`
  - Import `include`
    `from django.urls import include`
  - Add path with `include` and `namespace`
    - `/core`
      `path([URL], include([urls.py], namespace="[=app_name]"))`
    - `/[App]`
      ``
- `/[App]/url.py`
  - Create `urls.py` in each application folder(core included)
  - Import `path` and `views`
    `from django.urls import path`
    `from [App] import views as [App]_views`
  - Create `urlpatterns` and `path`
    `urlpatterns = [~]`
    `path("", [views.py].[View], name="~")`
  - Add `app_name` same as `namespace`

# 10.1 Django Render 이해하기

- HttpResponse
  : Minimal Requirement for homepage exist
  `from django.http import HttpResponse`
  `return HttpResponse(content="~")`
- Render
  : HttpResponse with HTML file
  - Create `/templates`
  - Set TEMPLATES's DIRS
    - `/config/settings.py`
    - `os.path.join(BASE_DIR, "templates")` in `TEMPLATES`\_`DIRS`
      `from django.http import HttpResponse`
  - Create Html Files in `/templates` folder
  - Return Render
    ```
    def all_rooms(req):
      return render(req, [template].html)
    ```
- Render with Context
  - add context in `render` argument as `dict`
    `render(req, [template].html, context={'[name]': [variable]}`
  - use in html as double curlybracket
    `{{[context]}}`
- Render with Python Logic
  - if statement
    ```
    {% if %}
    {% else %}
    {% endif %}
    ```
  - for statement
    ```
    {% for  in %}
    {% endfor %}
    ```

* template: HTML complied by Django
* context: send variable to template

# 10.3 Django Template 만들기

- Create `base.html` and [App] Folder in `/templates`
- Extends `base.html`
  `{% extends "base.html" %}`
- Add Block
  - `{% block [Name] %}{% endblock %}` in `base.html`
  - `{% block [Name] %} ~ {% endblock %}` in extended one
- Add Partials
  - `{% include '[html]' %}`

* block: input where child give contents to parent

# 11.0 Django Pagination 알아보기

- How to configure pagination manually
  - Get `page` from URL
    `/?page=1`
    `page = [request].GET.get("page", [default])`
    - make sure convert `str` into `int`
      `page = int(page)`
  - Get QuerySet with offset and limit
    ```
    page_size
    limit = page_size * page
    offset = limit - page_size
    objects.all()[offset:limit]
    ```
  - Get `page_count`
    `from math import ceil`
    ```
    page_count = objects.count() / page_size
    page_count = ceil(page_count)
    ```
  - Context variable
    ```
    "page": page,
    "page_count": page_count,
    "page_range": range(1, page_count)
    ```
  - Add `Previous` and `Next` Button
- Use Django Paginator
  [Link](https://docs.djangoproject.com/en/3.2/topics/pagination/)

  - Get `page` from URL
    `/?page=1`
    `page = [request].GET.get("page", [default])`
  - Get QuerySet
    `[QuerySet] = [Module].objects.all()`
  - Import `Paginator` and `paginate`
    `from django.core.paginator import Paginator`
    `paginator = Paginator([QuerySet], [Page_Size])`
  - Get Page Object
    - `get_page`
      `page = paginator.get_page(page)`
      When invalid return first page
    - `page`
      Raise Error when invalid page
  - Context `page` and Use it on template
    - `[Page].object_list`
    - `[Page].number`
    - `[Page].paginator.num_pages`
    - `[Page].previous_page_number`
    - `[Page].next_page_number`
    - `[Page].has_previous`
      : Return True if there's a previous page
    - `[Page].has_next`
      : Return True if there's a next page
  - Handle `orphans`
    `Paginator([QuerySet], [PageSize], [Orphan])`
    [Orphan] - `orphans=~`

* GET Request: data from URL
* Template Tag: apply logic on Template
  - [var]|add:~
* orphan: list of element not big as page_size
  when less or same as orphan merge with previous one

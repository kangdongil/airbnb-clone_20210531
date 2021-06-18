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
  - create something then save
    self.save()
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
  - FloatField()
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

# 3.0.2 Django AdminPanel 만들기

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
- Create button `View on Site` by `reverse`
  - Import `reverse`
    `from django.urls import reverse`
  - Override `get_absolute_url`
    ```
    def get_absolute_url(self):
      return reverse("[namespace]:[name]", kwargs={[STR]: [VARIABLE]})
    ```
  * reverse: convert url_name to actual url

* fieldsets: A group of fields
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
* Assign Name to Object
  set model a method `__str__`
  ```def __str__(self):
        return self.name
  ```
  - This name will appear on adminpanel

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
      - null=True is required.
    - SET_DEFAULT: default after deletion
  - gives access to other model's data
    `models.ForeignKey("users.User", ~)`
    `room.host(users).email`
- ManyToMany Relationship
  - `models.ManyToManyField([ModelName])`
  - to improve adminpanel,
    `filter_horizontal = (~)`
- OneToOneField: One model at a time

  - `models.OneToOneField([ModelName], on_delete="models.~")`
  - syntax is same as ForeignKey

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
- when objects.create(), [ImageField].save()
  Byte File need to be ContentFile
  `from django.core.files.base import ContentFile`

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
- Create Object with Manager
  - for statement is useful when data is given as `list[]`
    `[Model].objects.create([model]=~)`
  - when want to check repetition, `objects.get_or_create`
- Seed with `Random`
  `import random`
  - random choice
    - import QuerySets
      `[QuerySet] = [Module].objects.all()`
      - when QuerySet should get data selectively,
        `.filter([field]=[data])`
    - random.choice
      `"[field]": lambda x: random.choice([QuerySet])`
      - instead of QuerySet, `list[]` works, too.
  - random number
    `[field]: lambda x: random.randint([from], [to])`
- Seed ManyToMany field
  - for statement for QuerySet
    `amentities = Amenity.objects.all()`
    `for a in amenities:`
  - add `magic_number` and randomize with if statement
    `magic_number = random.randint(0, 15)`
    `magic_number % 2 == 0:`
  - add element from ManyToMany Field
    `[QuerySet].[Field].add([Element])`

# 9.1 Django Seed로 데이터 Seed하기

- Install `django_seed`
  `pip install django_seed`
- Add `django_seed` in `THIRD_PARTY_APPS`
  `/config/settings.py`
- Import Seeder and Module
  `from django_seed import Seed`
  `from [apps].models import [Module]`
- Add argument "total"
  ```
  parser.add_argument(
    "--total", default=10, type=int, help="~"
  )
  ```
- Import Argument on handle()
  `total = options.get("total")`
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
  - `seeder.faker` for appropriate data
    - use `lambda x`
    * list of faker
      - `seeder.faker.name()`
      - `seeder.faker.sentence()`
      - `seeder.faker.year()`
      - `seeder.faker.address()`
  - seeder.execute() return pks
    - set variable `pk_list`
      `pk_list = seeder.execute()`
    - flatten it
      `from django.contrib.admin.utils import flatten`
      `pk_list = flatten(list(pk_list.values()))`
    - use it on your own

* faker: library for fake stuff
  [Link](https://faker.readthedocs.io/en/master/providers/faker.providers.address.html)

# 10.0 Django Url과 View 알아보기

- Syntax of URL
  path("[URL]", [VIEW])

* url: way how direct request
* view: function how reply to request
  - when accessd View with URL, create `HttpRequest`
  - When `HttpRequest` occured, `HttpResponse` is mandatory

# 10.0.1 Django URL 관리하기

- `/config/urls.py`
  - Import `include`
    `from django.urls import include`
  - Add path with `include` and `namespace`
    - `/core`
      `path("", include([urls.py], namespace="[=app_name]"))`
    - `/[App]`
      `path([URL/]. include([urls.py], namespace="[=app_name]"))`
- `/[App]/urls.py`
  - Create `urls.py` in each application folder(core included)
  - Import `path` and `views`
    `from django.urls import path`
    `from [App] import views as [App]_views`
  - Add `app_name` same as `namespace`
    `app_name = [namespace]`
  - Create `urlpatterns` and `path`
    `urlpatterns = [~]`
    `path("", [views.py].[View], name="~")`
    - if [View] as class, add `.as_view()`
  - Create function in views
    - Import `render`
      `from django.shortcuts import render`
    - Create Function Based View(FBV),
      ```
      def all_[something](request):
        return render(request, "[template].html")
      ```

# 12.0 Django Path 알아보기

- `reverse` URL by using `namespace` and `name`
  `from django.urls import reverse`
  `reverse("[namespace]:[name]")`
- Add Variable on URL
  - <int:[variable]>
  - <str:[variable]>
  - make sure add argument on view
    `def room_detail(request, [variable]):`
- How to GET URL Arguments
  `/?city=seoul`
  - request.GET.get the URL Argument
  ```
  def [VIEW](request):
  [Variable] = request.GET.get("[Arg]", [Default])
  ```
- How to use `URL Tag` with `namespace` and `name`
  `{% url "[namespace]:[name]" [argument:optional] %}`

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
      return render(req, "[template].html")
    ```
- Render with Context
  - add context in `render` argument as `dict`
    `render(req, [template].html, context={'[name]': [variable]}`
    - instead of `context={~}`, just `{~}`
  - use in html as double curlybracket
    `{{[context]}}`
  - for ForeignKey, Mixin allowed
    `room.host.superhost`
  - for ManyToMany, add `.all`
    `room.amenities.all`
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
- Error Handling
  - Use `Try/Except` Statement
  - Specify Exception
  - `redirect` to somewhere
    `from django.shortcuts import redirect`
    ```
    except ~:
      return redirect(~)
    ```
  - Raise `404`
    `from django.http import Http404`
    `raise Http404()`
    - Customize Http404
      - create `templates/404.html`
      - To see on development,
        ```
        DEBUG = False
        ALLOWED_HOST = "*"
        ```
  * Exception List
    - [Module].DoesNotExist

* template: HTML complied by Django
* context: send variable to template

# 10.3 Django Template 만들기

- Add `.prettierignore` and add `templates` folder
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
    - filtered QuerySet should be ordered
      `[QuerySet] = [QuerySet].order_by(~)`
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
- When Class Based View,
  Page Object is given as `page_obj`

* GET Request: data from URL
* Template Tag: apply logic on Template
  - [var]|add:~
* orphan: list of element not big as page_size
  when less or same as orphan merge with previous one

# 11.7 Class based View(CBV) 만들기

- Create Class and inherit `View`
  `class [ViewName]([View]):`
  - Set model
    `model = [Model]`
    - Django View automatically return model lowercase as context
- Adjust URL's View as class
  `[Class].as_view()`
- Create template as `[AppName]/[App]_view.html`
- Add context with `get_context_data` method
  ```
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['[ContextName]'] = [VARAIBLE]
    return context
  ```
- Use `object_list` and `page_obj` as variable on template
  - object_list
  - page_obj
    : paginator stuff
    - how to change `page_obj` name
      context_object_name = "~"

* Classy CBV
  [Link](https://ccbv.co.uk/)
* ListView
  : A page representing a list of objects
  - [Attribute]
    - model
    - paginate_by
      : how many pages display in one page
      `paginate_by = 10`
    - paginate_orphans
      `paginate_orphans = 5`
    - ordering
      `ordering = "created"`
* DetailView
  - [Attribute]
    - pk_url_kwarg
      "pk"(default)
* URL Tag

# 11.8 Class based View(CBV) vs. Function based View(FBV)

- CBV(Class Based View)
  - Powerful Mixin and Inheritance
  - Skip Repetition
- FBV(Function Based View)
  - Configure Functionality easily

# 13.0 Form 만들기

- Extract data from URL
  - get URL argument
    `request.GET.get("[ARG]", "[Default]")`
  - normalize argument
    - str.captialize(~)
- Get data from DB
  - get queryset from manager
    `[Model].objects.all`
    `[Model].objects.filter`
- Context argument with categorization

  - create `form` dict and `choices` dict
    - form: Data from URL Extraction
    - choices: QuerySet from manager

  ```
  form = {"city": city, "s_country": country}
  choices = {"countries": countries}
  ```

  - unpack dicts and context
    `{**form, **choices}`

- Create Form on template
  <form method="get" action=[dest]></form>
    - one <button> is same as `submit`
- Save values and choices according to URL

  - <label for="~"><input id="~" />
    - `label-for` and `input-id` should be the same
    - `input-name` is URL arg when submitted
    - `input-value` is given value
  - <select id="~"><options>
    <option value="~">: data form(shorten one recommended)
    <option {% if [form] == [option] %}selected{% endif %}>
  - <input type="number">
    - int() data from URL
      `int(request.GET.get())`
      - <input attrib> as `id`, `value`, `name`
      - `value="{{[CONTEXT]}}"`
  - <input type="checkbox">
      - request.GET default as `False`(boolean)
      - <input attrib> as `id`, `name`
      - `{% if instant %}checked{% endif %}`
  - How to deal with ManyToMany Field

    - getlist ManyToMany Field(form)
      `request.GET.getlist([MODEL])`
      `s_[MODEL]`
    - get data from DB by manager(choices)
      `[MODEL].[FIELD].objects.all()`
    - Create Form for MtM Field

    ```
    <h3> TITLE
    <ul>
    {% for [OBJECT] in [OBJECT_LIST] %}
    <li><label><input type="checkbox">
    {% if amenity.pk|slugify in s_amenities %}
    checked
    {% endif %}

    ```

# 13.5 Filter 만들기

- Create QuerySet from `objects.filter`
  `rooms = Room.objects.filter(**filter_args)`
- Create dict `{filter_args}` and add up
  `filter_args = {}`
  - default exist, try if statement
    ```
    if [URLarg] != "[Default]":
        filter_args["[default]__[field_lookups]"] = [URLarg]
    ```
    if not, just filter_args
  - For ManyToMany Field
    ```
    if len([URLarglist]) > 0:
      for [URLarg] in [URLarglist]:
        [filtered_context] = [f_c]filter([MtM]__pk=int(URLarg))
    ```
- Configure Results on template
  ```
  <h3>Results</h3>
  {% for room in rooms%}
    <h3>{{room.name}}</h3>
  {% endfor %}
  ```

* Field Lookups: get the filtered data
  - `__startswith`
  - `__gte`: greater than equal
  - `__lte`: less than equal

# 13.7 Django Form 만들기

- Create `forms.py`
  - import `django.forms`
    `from django import forms`
  - create Class Form
    ```
    class [Name]Form(forms.Form):
    ~
    ```
- Import `form` on `views`
  `from . import views`
  `form = forms.[Name]Form(request.GET)`
  - Return context `{"form": form}`
- Create Forms Field
  - syntax is same as `modelfield`
    `forms.[Field](~)`
    - allow empty form
      `required=False`
- Customize Forms Widget
- filtered with cleaned_data
  != 0 to is not None
- {{form}} in <form> on template
  - How to change Forms Display
    {{form.as_p}}

* Django Form
  [Link](https://docs.djangoproject.com/en/3.2/ref/forms/api/)
* Widget: HTML element configured by Django Forms
* bounded form: Connected with Data and automatically validate it
* FieldType - Text
  - forms.CharField
    initial
  - forms.ModelChoiceField
    queryset
    empty_label
  - forms.ModelMultipleChoiceField
    queryset
    widget=forms.CheckboxSelectMultiple
* FieldType - Numeric
  - forms.IntegerField
* FieldType - Others
  - forms.BooleanField
  - CountryField
    - Import CountryField
      `from django_countries.fields import CountryField`
    - How to set Form Model
      `CountryField(default="~").formfield()`

# 14.0 LOG-IN & LOG-OUT 구현하기

- Create `login/` URL
  - `config/urls`
  - `users.urls`
- Create Views
- Create `login.html` for template
  - <form> as POST
    <form method="POST">
  - Login Button for template(`partials/nav`)
    `{% url "users:login" %}`
  - if statement with `user.is_authenticated`
    ```
    {% if user.is_authenticated %}
      Log out
    {% else %}
      Log in
    {% endif %}
    ```
- Create LoginForm
  ```
  email = forms.EmailField()
  password = forms.CharField(widget=forms.PasswordInput)
  ```
  - `views.py`
    - import forms
      `from . import forms`
      `form = forms.LoginForm()`
    - send form in context
- Fix CSRF verification failed
  `{% csrf_token %}`
- Validate Data(`clean_[Field]` method)
  - add method `clean_[FieldName]` in 'forms`
    - make sure `clean_` return data or cause None
    ```
    def clean_[field](self):
    [DATA] = self.cleaned_data.get("[FIELD]")
    try:
      check user=email exist
      return email
    except models.User.DoesNotExist:
      raise forms.ValidationError("[Error_Msg]")
    ```
  - get cleaned data in `views`
    ```
    form = forms.[Form](request.POST)
    if form.is_valid():
      form.clean_data
    ```
- Validate Data(`clean` method)
  - when data correlated to each other, `clean` method
    ```
    def clean(self):
    [DATA] = self.cleaned_data.get("[FIELD]")
    [DATA] = self.cleaned_data.get("[FIELD]")
    try:
      user = models.User.objects.get(email=email)
      if user.check_password(password):
        return self.cleaned_data
      else:
        [VALIDATION_ERROR]
    except [User.DoesNotExist]:
        [VALIDATION_ERROR]
    ```
  - check_password compare raw encrpyt password is right
  - self_add_error() to make specfic field error
    make sure error happen in specific fields(not in general)
  - return self.cleaned_data
- Use password_validator from django
- Configure Login and Logout
  - import `authenticate`, `login`, `logout`
    `from django.contrib.auth import authenticate, login, logout`
  - authenticate user
    `user = authenticate(request, username=email, password=password)`
    ```
    if user is not None:
      login(request, user)
      return redirect(reverse("core:home"))
    ```
  - create log_out method
    ```
    def log_out(request):
      logout(request)
      return redirect(reverse("core:home"))
    ```
    context_processor automatically send data by context

* CSRF: Cross Site Request Forgery
  - check POST request comes from valid website
* `clean_[field]` method
  - add Error if not validated
  - format data in appropriate way
* `user.check_password(password)`
  compare raw password and encrpyted password is correct

# 14.5 FormView로 로그인 구현하기

- Instead of LoginView, use FormView
  `class LoginView(FormView):`
  ```
  template_name = "[Template]"
  form_class = "[Form]"
  success_url = reverse_lazy("core:home")
  ```
- add `form_valid` method
  ```
  def form_valid(self, form):
    (authenticate)
    return super().form_valid(form)
  ```

* `reverse_lazy`
  `from django.urls import reverse_lazy`

# 15.0 Signup 구현하기

- Create SignUpView inherit FormView
  ```
  class SignUpView(FormView):
    template_name = "[TEMPLATE]"
    form_class = [FORM]
    success_url = reverse_lazy("core:home")
    initial = {~}
  ```
- Create `users/signup/` URL
- Create SignUpForm
  `first_name, last_name, email, password, password1`
  - add `label` to password1
- Validate Data by `clean`
- `save` method on forms
  `User.objects.create_user([USERNAME], [EMAIL], [PASSWORD])`
  `user.save()`
- check `form_valid`

# 16.0 Django Email 알아보기

- Add Email-related settings in `/config/settings.py`
  - In Mailgun, [Domain_settings]\_[STMP_credentials]
  ```
  EMAIL_HOST
  EMAIL_PORT
  EMAIL_HOST_USER
  EMAIL_HOST_PASSWORD
  EMAIL_FROM ** noreply
  ```
- Read EnvironmentVariable by `django-dotenv`
  - Create `.env` File
  - Put variable which handle private information
  - install `django-dotenv`
    `pip install django-dotenv`
  - Import dotenv in `manage.py`
    `import dotenv`
    ```
    if main
    dotenv.read_dotenv()
    ```
  - How to use env_var
    `os.environ.get("[ENVIRONMENT_VARIABLE]")`
    `email_confirmed = models.BooleanField(default=False)`
- Configure Verification Process
  - create `verify_email` logic in models.method
    - send_mail
      `from django.core.mail import send_mail`
      ```
      send_mail([TITLE], [TEXT], [NOREPLY], fail_silently=True, html_message)
      ```
  - send html_message
    - strip_tags
      - if email-user, doesn't use html email
        `from django.utils.html import strip_tags`
    - render_to_string
      - render html for email
        `from django.template.loader import render_to_string`
        `render_to_string([HTML], {[CONTEXT]})`

* Mailgun
  [Link](https://app.mailgun.com/)

# 17.0 OAuth로 로그인하기

- GitHub OAuth
  - How to OAuth Settings
    `[Settings]-[Dev_settings]-[OAuth]`
    - Homepage `http://127.0.0.1:8000/`
    - Authorization callback URL
      `http://127.0.0.1:8000/users/login/github/callback`
    - Get Github ID and Secret
  - OAuth Authorization Process
    1. Users are redirected to request their Github identity
    - Request `http://127.0.0.1:8000/users/login/github/callback`
    - Required Parameters
      - client_id
      - redirect_uri
      - scope
      - allow_signup(optional)
    2. Users are redirected back to your site by GitHub
    - create `github_callback` view
      - Install `Requests`
        `pip install requests`
        `import requests`
      - request POST with required parameters
        - client_id
        - client_secret
        - code
        - `headers={"Accept": "application/json"}`
      - return redirect home
    3. Your app accesses the API with the user's access token
- Kakao OAuth

  - Configure User Management

  * Kakao Developers
    [Link](https://developers.kakao.com/)

* OAuth
  Allow Social Media login account
* GitHub OAuth Docs
  [Link](https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps)
* access-token
  help access to github api

# 19.0 TailwindCSS란,

- utility-first CSS Framework highly customizable
- CSS-properties could be subtitute with `class-name`
- Reduce Repetition by `@apply` stuff
- Ready-made settings(such as `color-palette`, `default-sizing`) available

* How TailwindCSS applied
  - every CSS code should be written on `/asset/styles.scss`
  - `npm run css` will convert sass to css by gulp
  - `static` folder is for browser, `asset` folder is for programmer

# 19.1 TailwindCSS 설치하기

- VSCode Extension
  - Tailwind CSS Intellisense
- Setup for Installing TailwindCSS
  - Install Gulp
    `npm install -D gulp gulp-postcss gulp-sass gulp-csso node-sass`
  - Install Tailwindcss
    `npm install -D tailwindcss@latest postcss@latest autoprefixer@latest`
  - Create Tailwind config file
    `npx tailwind init`
  - Create `gulpfile.js`
  - Create folder `/assets` for scss file
    `/assets/scss/styles.scss`
  - Include Tailwind directive in CSS
    ```
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```
  - when scss file modified, `npm run css`
  - Set Static Files
    ```
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    ```
  - Load static/scss
    `{% load static %}`
    `<link rel="stylesheet" href="{% static 'css/styles.css' %}">`

# 19.3 TailwindCSS 사용하기

- container
  : Component fixed element's width to the current breakpoint
  - w
  - h
  - m
  - p
- @apply

* rem: root em
  - em: measurement relative to closest font-size
  - many responsive design website use this unit
  - `root em` is based on html
  - rem default font size is `16pt`

# 유용한 Python 명령어

- `print()`
- `dir([object])`
  Return list of name
- `vars([object])`
  Return `__dict__` for class
- `super().~`
  Execute code from Parent Class
- Handle Error
  ```
  try:
    ~
  except [Exception]:
    ~
  ```

# Project Overview

## Project Description

For project four of the General Assembly SEi course, I will be creating a full CRUD web application. I will create my backend using Django rest framework, and JWT Authentication with postgresql.

The backend will consist of a User table/ attendance table/ and events table. The user can be a student or an admin. An admin can also be a student. Only an admin can create/update/delete an event. Every time a student user adds their attendance for an event, the check-in table will get updated.

A bg influence for this projects MVP are sites like [meetup](https://www.meetup.com/) where you can see who attended an event.

A big influence for this projects post MVP are check-ins for gyms, where a member would scan their keychain before entering the gym area.
 
I hope to be able to implement this app in my martial arts school, where sign-ins are made via pen and paper in a notebook. The instructor must manually review 3,6, or 12 months worth of entries for each student when it's time to take the test. By automating this process, it will be easier to track the students attendance.
 
Link to [frontend](https://github.com/RosmaryFC/p4frontend)

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Fri-Sun, Sept 11-13, 2020 (Day 1-3)  | Project Description | Complete
|Mon, Sept 14, 2020 (Day 4)           | Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Mon-Tues, Sept 14-15, 2020 (Day 4-5) | Backend: RestAPI MVP| Complete
|Mon-Tues, Sept 14-15, 2020 (Day 4-5) | Frontend: Home page / Login Modal | Complete
|Wed, Sept 16, 2020 (Day 6)           | Frontend: User page / Admin page| Complete
|Thurs, Sept 17, 2020 (Day 7)         | Frontend: CSS, MVP, bug fixes | Complete
|Fri-Sat, Sept 18, 2020 (Day 8-9)     | Post-MVP backend/frontend | Partial complete
|Sun, Sept 20, 2020 (Day 8)           | Update documentation | Complete
|Mon, Sept 21, 2020 (Day 8)           | Final Touches| Complete
|Tues, Sept 22, 2020 (Day 11)         | Present | Incomplete

## Models 

User Model should have
- username, email, password, first name, last name
   * Post MVP: date of birth, gender, rank, pin

Attendance Model should have
- user, date, time

Events Model
- event type, event name, date, price, address
   * Post MVP: users []


## Time/Priority Matrix 

[Time/Priority Matrix](https://res.cloudinary.com/rosefc/image/upload/v1600115571/project%204/backend_time_priority_matrix.png)

### MVP/PostMVP 

#### MVP

- Build/test user Authentication
- User model, routes, controllers
- Attendance: model, routes, controllers
- Events: model, routes, controllers
- Deploy backend on Heroku

#### PostMVP 

- Refactor
- create events attendance table or add it to events table: table will have student, event type (seminar, tournament), event name
- Admin can add if student has gone to an event
- Create status table: Student status will have rank, kihon, kata, ippon kumite, Renzoku-waza, events, attendance

## Functional Components

#### MVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Initial setup: installing packages | H | .25hr | .25hr | .25hr|
| Initial setup: create superuser    | H | .25hr | .25hr | .25hr|
| Initial setup: deployment on Heroku| H | .25hr | .25hr | .25hr|
| Auth/User: create model            | H | 1hr | 2hr | 2hr|
| Auth/User: create controllers      | H | 2hr | 2hr | 2hr|
| Auth/User: create routes           | H | 1hr | 2hr | 2hr|
| Auth/User: test Postman            | H | 2hr | 2hr | 2hr|
| Attendance: create model             | H | 1hr | 2hr | 2hr|
| Attendance: create controllers       | H | 2hr | 2hr | 2hr|
| Attendance: create routes            | H | 1hr | 2hr | 2hr|
| Attendance: test Postman             | H | 2hr | 2hr | 2hr|
| Events: create model               | H | 1hr | 2hr | 2hr|
| Events: create controllers         | H | 2hr | 2hr | 2hr|
| Events: create routes              | H | 1hr | 2hr | 2hr|
| Events: test Postman               | H | 2hr | 2hr | 2hr|
| Create and seed data               | L | 1hr | -hr | -hr|
| Total                              |   | 19.75hrs| 24.75hrs | 24.75hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Refactor                                  | L | 3hr | -hr | -hr|
| checkin attendance                        | L | 8hr | -hr | -hr|
| Admin adding if student has gone to event | L | 2hr | -hr | -hr|
| status: create model                      | L | 1hr | -hr | -hr|
| status: create controllers                | L | 2hr | -hr | -hr|
| status: create routes                     | L | 1hr | -hr | -hr|
| status: test Postman                      | L | 2hr | -hr | -hr|
| Total                                     |   | 12hrs| -hrs | -hrs |

## Additional Libraries
- [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- [Django rest framework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [JWT authentication](https://jwt.io/introduction/) - JSON Web Token (JWT) is an open standard (RFC 7519) that defines a compact and self-contained way for securely transmitting information between parties as a JSON object.
- [postrgresql](https://www.postgresql.org/) - PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.
- [python](https://www.python.org/) - Python is a programming language that lets you work more quickly and integrate your systems more effectively.

## Code Snippet 

This is one of the many edits I made to the backend to make it work better with what I wanted. I created a route so that I can get a list of all users to later use that information to display users on a list
I feel confident enough to create my own routes, views, serializes, and models!

```
ADDING A ROUTE TO GET ALL USERS

authentication/serializers.py
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_admin')

authentication/views.py
class UserViewSet(ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserListSerializer

    queryset = User.objects.all()

urls/views.py
urlpatterns = [
    . . .
    url(r'^users/$', UserViewSet.as_view({'get': 'list'}), name='users')
    . . .
]

```

## Issues and Resolutions

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

**ERROR**: delete event method can only be deleted by user that created it. user can only view events that they created,
when deleting an event, no response would return
```
    def destroy(self, request, *args, **kwargs):
        event = Event.objects.get(pk=self.kwargs["pk"])
        if not request.user.is_admin == event.owner:
             raise PermissionDenied("you cannot delete this event")
        return super().destroy(request, *args, **kwargs)

```
***RESOLUTION**: I updated my delete method to allow any user to view, and return a response
https://stackoverflow.com/questions/52683250/django-rest-framework-delete-returns-no-content-in-the-body
```
    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
```
***ERROR***: Trying to delete an attendance row but I keep getting a 301 error and then get rerouted to a get
```
DELETE http://127.0.0.1:8000/api/attendances/6
```
I wasn't too sure what the proper route was I tried many different delete routes in which I referenced my view class for
I figure I was just using the incorrect route. I did some more research and came across this solution
https://stackoverflow.com/questions/4891879/http-delete-request-to-django-returns-a-301moved-permenantly

***RESOLUTION***: append a slash T.T
```
DELETE http://127.0.0.1:8000/api/attendances/6/
```

***ERROR***: Delete request for attendance does not return a response
```
DELETE METHOD
def destroy(self, request, *args, **kwargs):
    print("destroy attendance viewset")
    attendance = Attendance.objects.get(pk=self.kwargs["pk"])
    if not request.user == attendance.owner:
        raise PermissionDenied(
            "you have no permission to delete this attendance"
        )
    return super().destroy(request, *args, **kwargs)

STATUS 204: no content
```
***RESOLUTION***: fix delete request method to return a response
```
    def destroy(self, request, *args, **kwargs):
        print("destroy attendance viewset")
        attendance = Attendance.objects.get(pk=self.kwargs["pk"])
        serializer = self.get_serializer(self.get_object())
        # TODO: only admin can destroy an attendance
        if not request.user == attendance.owner:
            raise PermissionDenied(
                "you have no permission to delete this attendance"
            )
        super().destroy(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)

STATUS 200:OK
```

***ERROR***: Having an error when trying to migrate to heroku deployed backend
```
(venv) Rosmarys-MacBook-Pro:p4backend Rosemary$ heroku run python manage.py migrate --app=rf-p4backend
Running python manage.py migrate on ⬢ rf-p4backend... up, run.3744 (Free)
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/__init__.py", line 401, in execute_from_command_line
    utility.execute()
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/__init__.py", line 395, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 330, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 371, in execute
    output = self.handle(*args, **options)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/base.py", line 85, in wrapped
    res = handle_func(*args, **kwargs)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/core/management/commands/migrate.py", line 95, in handle
    executor.loader.check_consistent_history(connection)
  File "/app/.heroku/python/lib/python3.6/site-packages/django/db/migrations/loader.py", line 306, in check_consistent_history
    connection.alias,
django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency authentication.0001_initial on database 'default'.

```
https://stackoverflow.com/questions/51040436/django-db-migrations-exceptions-inconsistentmigrationhistory-issue-after-creatin/51041776


reset heroku database
ran command: heroku run python manage.py migrate --app=rf-p4backend

```
(venv) Rosmarys-MacBook-Pro:p4backend Rosemary$ heroku run python manage.py migrate --app=rf-p4backend
Running python manage.py migrate on ⬢ rf-p4backend... up, run.9781 (Free)
Operations to perform:
  Apply all migrations: admin, api, auth, authentication, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying authentication.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying authentication.0002_user_is_admin... OK
  Applying api.0001_initial... OK
  Applying api.0002_auto_20200916_1656... OK
  Applying api.0003_auto_20200916_1656... OK
  Applying api.0004_auto_20200917_0437... OK
  Applying api.0005_event_img... OK
  Applying api.0006_auto_20200920_0454... OK
  Applying api.0007_auto_20200920_0503... OK
  Applying sessions.0001_initial... OK
(venv) Rosmarys-MacBook-Pro:p4backend Rosemary$ 
```
ran command:  heroku run python manage.py createsuperuser --app=rf-p4backend
```
(venv) Rosmarys-MacBook-Pro:p4backend Rosemary$ heroku run python manage.py createsuperuser --app=rf-p4backend
Running python manage.py createsuperuser on ⬢ rf-p4backend... up, run.3465 (Free)
Username: *******
Email: **************
Password: 
Password (again): 
Superuser created successfully.

```

***SOLUTION*** reset the database on heroku and that fixed it!


***ERROR*** when making request to backend for route `http://127.0.0.1:8000/api/eventspublic/` anyone can make CRUD requests to it
```
# TODO: create a get request to get all events but without token
class EventViewSetPublic(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset
```
***SOLUTION*** changes AllowAny to IsAuthenticatedOrReadOnly
https://medium.com/@taranjeet/django-implementing-view-only-permissions-d3f5e6371b3
https://www.django-rest-framework.org/api-guide/permissions/
```
# TODO: create a get request to get all events but without token
class EventViewSetPublic(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset
```


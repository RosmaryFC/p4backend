# Project Overview

## Project Description

For project four of the General Assembly SEi course, I will be creating a full CRUD web application. I will create my backend using Django, Django rest framework, and JWT with postgresql.

The backend will consist of a User table/ check-in table/ and events table. The user can be a student or an admin. Only an admin can create/update/delete an event. Every time a user checks in to a class, the check-in table will get updated.

A big influence for this project are check-ins for gyms, where a member would scan their keychain before entering the gym area.
 
 I hope to be able to implement this app in my martial arts school, where sign-ins are made via pen and paper in a notebook. The instructor must manually review 3,6, or 12 months worth of entries for each student when it's time to take the test. By automating this process, it will be easier to track the students attendance.
 
 Link to [frontend](https://github.com/RosmaryFC/p4frontend)

## Project Schedule

|  Day | Deliverable | Status
|---|---| ---|
|Fri-Sun, Sept 11-13, 2020 (Day 1-3)  | Project Description | Complete
|Mon, Sept 14, 2020 (Day 4)           | Wireframes / Priority Matrix / Timeline `backend` and `frontend`| Complete
|Mon-Tues, Sept 14-15, 2020 (Day 4-5) | Backend: RestAPI MVP| Incomplete
|Mon-Tues, Sept 14-15, 2020 (Day 4-5) | Frontend: Home page / Login Modal | Incomplete
|Wed, Sept 16, 2020 (Day 6)           | Frontend: check-in page / Admin page| Incomplete
|Thurs, Sept 17, 2020 (Day 7)         | Frontend: CSS, MVP, bug fixes | Incomplete
|Fri-Sat, Sept 18, 2020 (Day 8-9)     | Post-MVP backend/frontend | Incomplete
|Sun, Sept 20, 2020 (Day 8)           | Update documentation | Incomplete
|Mon, Sept 21, 2020 (Day 8)           | Final Touches| Incomplete
|Tues, Sept 22, 2020 (Day 11)         | Present | Incomplete

## Models 

User Model should have
- username, email, password, first name, last name
   * Post MVP: date of birth, gender, rank, pin

Check-in Model should have
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
- check in: model, routes, controllers
- events: model, routes, controllers
- Deploy backend on Heroku

#### PostMVP 

- Refactor
- create events attendance table or add it to events table: table will have student, event type (seminar, tournament), event name, event ID
- Admin can add if student has gone to an event
- Create status table: Student status will have rank, kihon, kata, ippon kumite, Renzoku-waza, events, attendance

## Functional Components

#### MVP
| Component | Priority | Estimated Time | Time Invested | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Initial setup: installing packages | H | .25hr | .25hr | .25hr|
| Initial setup: create superuser    | H | .25hr | .25hr | .25hr|
| Initial setup: deployment on Heroku| H | .25hr | .25hr | .25hr|
| Auth/User: create model            | H | 1hr | -hr | -hr|
| Auth/User: create controllers      | H | 2hr | -hr | -hr|
| Auth/User: create routes           | H | 1hr | -hr | -hr|
| Auth/User: test Postman            | H | 2hr | -hr | -hr|
| Check in: create model             | H | 1hr | -hr | -hr|
| Check in: create controllers       | H | 2hr | -hr | -hr|
| Check in: create routes            | H | 1hr | -hr | -hr|
| Check in: test Postman             | H | 2hr | -hr | -hr|
| Events: create model               | H | 1hr | -hr | -hr|
| Events: create controllers         | H | 2hr | -hr | -hr|
| Events: create routes              | H | 1hr | -hr | -hr|
| Events: test Postman               | H | 2hr | -hr | -hr|
| Create and seed data               | L | 1hr | -hr | -hr|
| Total                              |   | 19.75hrs| -hrs | -hrs |

#### PostMVP
| Component | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Refactor                                  | L | 3hr | -hr | -hr|
| events attendance                         | L | 1hr | -hr | -hr|
| Admin adding if student has gone to event | L | 2hr | -hr | -hr|
| status: create model                      | L | 1hr | -hr | -hr|
| status: create controllers                | L | 2hr | -hr | -hr|
| status: create routes                     | L | 1hr | -hr | -hr|
| status: test Postman                      | L | 2hr | -hr | -hr|
| Total                                     |   | 12hrs| -hrs | -hrs |

## Additional Libraries
- Django
- Django rest framework
- JWT authentication
- postrgresql

## Code Snippet - STILL BEING WORKED ON

Use this section to include a brief code snippet of functionality that you are proud of an a brief description  

```
function reverse(string) {
	// here is the code to reverse a string of text
}
```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier                                
**RESOLUTION**: Missing comma after first object in sources {} object

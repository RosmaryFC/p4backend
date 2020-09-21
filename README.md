# **Hiraldo's Kai**

## [Link to Frontend](https://github.com/RosmaryFC/p4frontend)

### Project Snapshots

 UPDATE! WIll go here
***

### Description

Checking into events for students will be much easier now with the ability to select which event you went to based on your profile!

Hiraldo's kai has incorporated a login system for students to always be up to date with upcoming events as well as attendance!
Students can log in and select which events they have attended in order to meet requirements for belt advancement.

Admin users can Create, Update or Delete events once they are no longer needed.

Hiraldo's Kai is a great place to stay up to date with the martial arts community.
***

### Websites
[backend](https://rf-p4backend.herokuapp.com/)

[frontend](https://hiraldokai.netlify.app/) 
***
### Technologies
The backend is made with Ruby on Rails, and PostgreSQL. It is deployed through Heroku. 

[<img src ="https://banner2.cleanpng.com/20180711/rtc/kisspng-django-web-development-web-framework-python-softwa-django-5b45d913f29027.4888902515313042119936.jpg" width="60" height="50">](https://www.djangoproject.com/)
[<img src ="https://qph.fs.quoracdn.net/main-qimg-28cadbd02699c25a88e5c78d73c7babc" width="50" height="50">](https://www.python.org/)
[<img src ="https://cdn.worldvectorlogo.com/logos/postgresql.svg" width="70" height="50">](https://www.postgresql.org/)
[<img src ="https://cdn.worldvectorlogo.com/logos/heroku.svg" width="50" height="50">](https://www.heroku.com/)
[<img src ="https://jwt.io/img/logo-asset.svg" width="100" height="50">](https://jwt.io/introduction/)
[<img src ="https://res.cloudinary.com/practicaldev/image/fetch/s--rAk2-3Xf--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://thepracticaldev.s3.amazonaws.com/i/gz5xantp1vycu7ueleh4.jpg" width="100" height="50">](https://www.django-rest-framework.org/)

***

### Features

- Users can create an account only if they have a secret key given to them by the school
- Users can create either an admin account or a student account
- admins can create events that will show up on the home page for anyone to see
- admins can also update and delete events
- admins are also students and have all the functionality a student would have
- students can update their attendance for each event they have gone to
- events are displayed on the home page for everyone to see!

***

### Future Implementation

- daily check-in to beginner, intermediate, advanced classes
- user can upload a flyer for an event
- daily check-in with QR code
- User dashboard will have user status (belt, rank, personal info, requirements for advancement, attendance)
- admin can modify  event attendance, and modify or update student user status's
- Nicer frontend design

***

## The Backend

### User Model

The user model allows two types of users to be created:
1. A SuperUser: that has full control of the backend via the admin routes
2. A User: that has access via the frontend. Two different types of users can be created:
    * Admin User: can Create Update Delete an event if authenticated
    * Student User: can Update Delete their attendance for an event if authenticated

### Events Model

The events Model consists of:
* an Owner: the user creating the event
* a name: the name of the event
* flyer: the URL of the flyer
* type: event type (tournament, seminar, party)
* date: event date
* time: event start time
* price
* address
* created: time of creation
* updated: time of latest update to event

I wanted to be as detailed as possible for each Event item. Each Event has an attendance list. Events are already automatically displayed on the home page regardless of user login.

### Attendance Model

The attendance model consists of:
* an Owner: the user creating the event
* event: the id of the event the user attended
* created: time of creation
* updated: time of latest update to event

I wanted the attendance to work more like a boolean so when the user creates an attendance it will show up in the attendance table
When the user deletes an attendance, the row will be removed from the table.


# Lettuce Eat

![devices](https://i.imgur.com/Uut5HeV.png)

[Lettuce Eat](https://ci-booking-system.herokuapp.com/) is a digital booking system for restaurants.

This is a recreation of [Lettuce Eat (Flask)](https://github.com/GeorgieGray/booking-system). This version uses Django.

Restaurant owners enter data about their restuarant and customers book tables. In this version restaurant owners must manage table availability manually, contacting customers where they're unable to support a booking.

The web application frontend has four high-level views:
- Landing view
- User login
- User registration
- Table booking

The website is hosted using Heroku, see it here:  
TODO

## Table of Contents
- [Target Demographic](#target-demographic)
- [Project planning](#project-planning)
- [Project management](#project-management)
- [Features](#features)
- [Technology](#technology)
- [Project Structure](#project-structure)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Methodology](#methodology)
  - [Third-Party](#third-party)
- [Citations & Credits](#citations--credits)

## Target Demographic
- Restuarant owners looking to modernise their booking experience
- Restuarant owners looking to improve their online advertising conversion rate, by lowering the barrier for customers to give them business
- Restuarant customers who dislike phone conversations (book online instead)
- Restuarant customers who are technology-aware

## Project planning
This section discusses my approach to thinking about and designing the system. The diagrams I created are mostly accurate to the final system, some small changes were made as I made further discoveries during development.

An example of a small change is how the booking view moved from it's originally planned place in the landing view to a private dedicated booking view.
### Mind map
![](https://i.imgur.com/zWQv8oC.jpg)

I started this project by exploring what functionality a user would be looking for in a restaurant booking system: what are the things they'll want to know about the restaurant, and how should they experience the booking journey.

During this phase I also considered which constraints would be meaningful for a restuarant owner to be able to set. For example: A restaurant owner may want to limit time spent per table.

### Data model
![](https://i.imgur.com/DOEj8hJ.jpg)

In this next phase I designed a data model to hold the information necessary to deliver on the ideas captured in the mind mapping phase. The lines represent relationships between tables.

The data model includes the following: restaurant meta data, regular opening days & hours, once-off days when the restauarant is closed (training, renovation, public holiday), the tables at the premises and their meta data, the users of the system and of course the key piece of data: the bookings themselves.

### Data operations
![](https://i.imgur.com/AOxCvJR.jpg)

From here I considered the key functionalities of the system with respect to the data model. Pictured here are each key feature and their data dependencies.

### UI/UX
![](https://i.imgur.com/QBRJLXF.jpg)

Finally I imagined how the user experience would be, and how the previously considered functionalities would be exposed to the end-user.

## Project management
- See [Github Project](https://github.com/users/GeorgieGray/projects/1)

## Features
### Landing view
![](https://i.imgur.com/85TbWcQ.png)

The welcome view. This is the start of the users journey.

Once the user has registered and is logged in, they're no longer shown the registration controls.

![](https://i.imgur.com/96uVbLe.png)

### User registration
![](https://i.imgur.com/lQpyiID.png)

A form to collect the users information and allow them to create an account. Once they've successfully submit the form they're automatically logged in and taken to the booking view.

### User login
![](https://i.imgur.com/4Fqton7.png)

A form to allow the user to log in if they already have an account. On successful login they're taken to the booking view. A logged in user is unable to see this view, they're immediately forwarded to the booking view.

### Table booking
![](https://i.imgur.com/Y9vs566.png)

The main functionality of the web application. This view allows users to see and manage their previous bookings, and create new ones.

## Local Development

Install dependencies
> pip install -r requirements.txt

Run django app
> python manage.py runserver

## Deployment
The game is deployed to Heroku.

Here are some instructions so you can do it yourself:
1. Create an account on Heroku
2. "New" in the top right corner of dashboard > create new app
3. Install the [heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. Authenticate with the CLI: `heroku login`
5. Follow the [Deploying with Git](https://devcenter.heroku.com/articles/git) instructions to setup your git repo correctly to speak with Heroku.
6. Set the env variables: settings > config vars (See: `env.example` in src code)
6. When you're ready to deploy: `git push heroku main`

## Testing
### Methodology

Here is my regression testing method:

1. Go to home view, see both hero buttons + signup and login links
1. Register an account `/signup`
2. Test validation for each of the inputs
3. Submit, see that you're redirected to `/booking`
4. Return to home view, see only one hero button + logout and book a table
5. Log out
6. Go to login view, login, get redirected to `/booking`
7. Change browser url to `/login`, see that you're redirectedt to `/booking` automatically.
8. Go to `/booking`
9. Choose date, time, table, group size -> submit
11. See booking appear to right
12. Delete booking to right, see it disappear
13. Log out, register a new user and log back in.
14. Ensure that bookings from previous steps are scoped to the previous user only.

### Third party
#### Lighthouse
![](https://i.imgur.com/AWyKxqo.png)

#### W3C Jigsaw
There is an error here but it belongs to Bootstrap, so is out of my control. Otherwise good.

https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fci-booking-system.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en

#### W3C Markup Validator
Info + minor warning, otherwise good.
https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-booking-system.herokuapp.com%2F


## Citations & Credits

### Learning resources
- Heroku documentation
  - https://devcenter.heroku.com/articles/heroku-cli
  - https://devcenter.heroku.com/articles/git

- Flask documentation
  - https://flask.palletsprojects.com/en/2.2.x/

- Flask login documentation
  - https://flask-login.readthedocs.io/en/latest/

- Digital ocean learning resources
  - This provided a good example to validate my learning against
  - https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

- SQLAlchemy documentation
  - https://docs.sqlalchemy.org/en/20/

### Free assets
- App logo source
  - https://www.creativefabrica.com/product/vector-lettuce-filled-outline-icon/
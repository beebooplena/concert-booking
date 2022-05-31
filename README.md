# The Music Gallery Booking Site
This is the webpage I created for the fourth milestone project(Fullstack frameworks with django)at code institute, diploma in Software Development. I wanted to make a music concert booking system. The inspiration for this, is that music is one of my big hobbies. It is also a mobile responsive website. You can visit the website here:-----
The website has a landing page, booking page, edit and delete booking page and an about page with a CRUD(create, read, update and delete) focus for the user.



![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/responsive_gwzk6x.png)
## Ui and Ux
## Research
I have a bachelor degree in music, and I have been on a stage several times. I have also attended several concerts as a listener. With this in mind, I would have liked a landing page, where you instantly knew it was a booking site. My experience and my analyse of the live venue scene, I would suggest an easy to use booking site. A clean and well looking site, where the users can book and edit or delete booked tickets. This kind of booking sites, can help small venue events with controlling how many people that will arrive at a concert.



## Owner's goal
* The owner wants the ability to control how many people that will arrive at a concert
* The owner wants the ability to have a total amount of tickets.
* The owner wants the ability to build the brand of the 'The Music Gallery.'




## User's goals
* The users would like to know how to contact the venue.
* The users would like to read about the venue.
* The users would like to read about the upcoming concert.
* The users would like to be able to order more than one ticket.
* The users wants an easy to use booking site.
* The users wants a safe to use booking site.
* The users would like to be able to book tickets.
* The users would like to be able to edit tickets.
* The users would like to be able to delete tickets.
* The users would like to register an account.
* The users would like to log in and log out of that account.


## User stories
The users in this webpage is the owner and the spectators. There can be many more userstories, but I choose these as my primary goals and aims for this booking site.
Admin: 
Concert manager:
* As a site admin I can update information about the concert venue so that the information can always be up to date.
* As a site admin I can create, delete and update concerts so that I can display new concerts or delete old concerts from the site

User:
Navigation and view:
* As a site user I can read about the concert venue so that I can get information about the facilities.
* As a site user I can send feedback so that The booking site owner receives my message.
* As a site user I can see a google map so that I know where the concert venue is located.
* As a site user I can easily understand that this site is a booking site for music concerts so that I can decide if I will book  or not.
Booking:
* As a site user I can delete my booked tickets in case I can`t go to the consert
* As a site user I can edit my booked ticket or tickets  so that I can change the amount of booked tickets
* As a site user I can book one or more tickets so that I can watch the consert
Account registration:
* As a site user I can register an account so that I can book tickets

![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653949959/user-story_gqbqr9.png)

### Strategy plane
I could not finish all my userstories, this was because of lack of time and knowledge.The two userstories that was left behind are also the two least important userstories. Below is a list (1-5), where one is least important and 5  is the most important userstory.
#### 5
* As a site admin I can update information about the concert venue so that the information can always be up to date.
* As a site admin I can create, delete and update concerts so that I can display new concerts or delete old concerts from the site
* As a site user I can book one or more tickets so that I can watch the consert
* As a site user I can easily understand that this site is a booking site for music concerts so that I can decide if I will book  or not.
* As a site user I can register an account so that I can book tickets
* As a site user I can delete my booked tickets in case I can`t go to the consert
#### 4
* As a site user I can edit my booked ticket or tickets  so that I can change the amount of booked tickets
* As a site user I can read about the concert venue so that I can get information about the facilities.
* As a site user I can send feedback so that The booking site owner receives my message.
* As a site user I can see a google map so that I know where the concert venue is located.

### Future Features
(1-5), where one is least important and 5  is the most important userstory.
#### 5
* As an admin, I can be safe that the total tickets will be adjusted as the users are booking, editing or deleting tickets.
* As a site user,I can pay for my ticket on the webpage.
* As a site user I can give feedback to the owner.
* As an admin, I can have the spectators book and buy for the tickets on the webpage.
* As a user, I can see how many tickets there are left to book.

#### 4
* As a site user I can see a map on the webpage, so I know where the venue is.
* As a site user, I can  read more about the bands that are going to play.

#### 3
* As a site user, I can view my profile and add profile image and information.
* As a site user, I can  read more about the bands that are going to play.
* As an admin, I can add videos from concerts on the webpage.

### Scope plane
The userstories needs different pages to fulfill the userstories goals.
* Landing page(home page) where the users can see and understand with a blink on an eye, that this is a music concert booking site. An easy landing page where users can easily understand and navigate in. They can also read about the concert.
* Registration page where the user can make an account.
* Login page where the users can log in. The owner can also login.
* Only the owner can log in and manage concerts and tickets.
* Sign out page where the users can sign out.
* Booking page, where the users can book tickets through a form. The users will be navigated to a registraion if they are not logged in. The users gets a success message, when a ticket is booked. The users gets error message if they try to book 0 tickets or if they try to book over the total amount of tickets.
* An Edit and delete page, where the users can see the amount of tickets they have, and can edit or delete their tickets if they want. The users gets success message when they haved edited or deletet tickets.
* About page, where the users can read more about the venue.


### Structure plane

* Landing page(index.html)
Home page of the website. There is a navbar, concert image, venue image and a booking 'card' with information about the concert with a booking button located on the card. The header and footer is on every page in the website.
* Booking page(booking.html)
Almost identical to the home page. Only now you can pick the concert the user wants to see and decide how many tickets the user wants to book.
* View booked tickets and can choose to edit or delete(show_booking.html)
Almost identical to the home page, but in the card, the user can see information about the users booked tickets. There is two buttons: edit and a delete button. The user can now choose to edit or delete their booked tickets.
* Edit page(edit_booking.html)
Similar as the home page, but now the user can update their tickets.
* About page(about_booking.html)
The user can read more about the venue.
* Admin (/admin)
This Admin page is made by django. The admin/owner can add new concerts, venues and tickets.
* Base template (base.html)
This base template is used to make a html that can be used on several html templates.
* Css and Javascript(.css and .js)
css and javascript are connected to the html files/templates.
* Registrtion(signup.html)
The users can register and create an account, so they can book and save their tickets. this is done by Django Allauth.
* Login(login.html)
The users can log in and can book tickets and see their bookings. This is also done by django Allauth.

Below you can see a flow chart of the webpage and see how the templates are connected.
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653956033/flow_l1uj6d.png)

As you can see on the flow chart, only logged in users can book tickets and save their booking information. The users will be navigated to the registraion page if their are not logged in. If the users try to go to booking page by typing the address, this will not work, since the users must be authenticated. When a user book tickets, this information will be posted to the admin. The users can see their booking on the page after they have booked tickets. The users can now decide if they want to delete or edit their booking. A success message will arrive when a user book, edit, delete, login or logout. An error message will occur if the users try to order 0 tickets or book tickets more than the total amount of tickets.
A user can only book tickets for themselves. A user can not book tickets for other users.

## Skeleton plane 

![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/landing-page_tewq56.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947439/login_vghbjs.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/registration_bfoxth.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/signout_wphijm.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947441/about_a2rqhn.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947441/booking_eat9hh.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947441/edit-delete_fgn5ga.png)


<br>


## Surface Plane

### Font

### Colours



### Icons


## Features
### Logo


### Home Image



### Welcome text


### Timetable



### Diary page



### Sign-up page



 ### Footer




### Navigation bar






## Technology
I used different technologies to make this webpage:

* Coolors
* Balsamiq
* Fontawesome
* Google Fonts
* Am I responsive
* VS-code
* Git Hub
* Chrome Dev Tool
* Css Validator
* Html Validator

## Languages

* HTML5
* CSS




## Testing 




### Validator Testing 
**HTML**

* The offical W3C validator showed no errors when tested.

**CSS**

* The official Jigsaw validator showed no errors when tested.

**Accessibility**
* By using lighthouse in devtools I could see that the webpage scored very well on all the tests.



### Bugs



### Unfixed Bugs
* No unfixed bugs.

### Commit messages






## Deployment



## Credits 






### Content



* I also got inspired from the CL love running project to start with this default code to make it easier to use css. Here is the original code from the CL love running project:

*{ margin:0;
padding: 0;
border: none; }

* I used icons from font awesome

* I used coolors.co to find a nice colour palette to my webpage.

* I used youtube as a social media link.

* I imported a font from google font.
### Media


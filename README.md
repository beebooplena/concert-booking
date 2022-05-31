# The Music Gallery Booking Site
This is the webpage I created for the fourth milestone project(Fullstack frameworks with django)at code institute, diploma in Software Development. I wanted to make a music concert booking system. The inspiration for this, is that music is one of my big hobbies. It is also a mobile responsive website. You can visit the website here:-----
The website has a landing page, booking page, edit and delete booking page and an about booking page. The booking page has a CRUD(create, read, update and delete) focus for the user.



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

### Kanban planner
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653949959/user-story_gqbqr9.png)

### Strategy plane
I could not finish all my userstories, this was because of lack of time and knowledge.The two userstories that was left behind are also the two least important userstories. Below is a list (1-5), where one is least important and 5  is the most important userstory.
##### 5
* As a site admin I can update information about the concert venue so that the information can always be up to date.
* As a site admin I can create, delete and update concerts so that I can display new concerts or delete old concerts from the site
* As a site user I can book one or more tickets so that I can watch the consert
* As a site user I can easily understand that this site is a booking site for music concerts so that I can decide if I will book  or not.
* As a site user I can register an account so that I can book tickets
* As a site user I can delete my booked tickets in case I can`t go to the consert
##### 4
* As a site user I can edit my booked ticket or tickets  so that I can change the amount of booked tickets
* As a site user I can read about the concert venue so that I can get information about the facilities.
* As a site user I can send feedback so that The booking site owner receives my message.
* As a site user I can see a google map so that I know where the concert venue is located.

### Future Features
(1-5), where one is least important and 5  is the most important userstory.
##### 5
* As an admin, I can be safe that the total tickets will be adjusted as the users are booking, editing or deleting tickets.
* As a site user,I can pay for my ticket on the webpage.
* As a site user I can give feedback to the owner.
* As an admin, I can have the spectators book and buy for the tickets on the webpage.
* As a user, I can see how many tickets there are left to book.

##### 4
* As a site user I can see a map on the webpage, so I know where the venue is.
* As a site user, I can  read more about the bands that are going to play.

##### 3
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
I choosed calm colours as base colors for the website. To the nav bar and buttons I choosed bright colors that would stand out a little, like
yellow, green, pink and blue. The Delete button has a red strong color and the edit button has a green bright button.
I used https://coolors.co/ to find ideas to how my colors would look nice on a website.

![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653957215/css_ujl8e8.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653957223/css1_mdxbmh.png)
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947441/edit-delete_aoyte5.jpg)

### Font
I used the font Laila that look informal and a fun font for the users. I also choosed a fire effect on the header in the bootstrap card.

### Icons
I used fontawesome to make icons.


## Features
### Logo
The main title is quite large for the users to see. The title has a little shading effect to make it stand out a little.


### booking card
The bootstrap card has a darker color that stands out from the green calm colors from the website.
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947441/booking_e97qon.jpg)
### Edit or delete booking card
The bootstrap card has a darker color that stands out from the green calm colors from the website.
The buttons has different colors. The delete button has a strong red color that symbolise danger. The edit button has a green bright color.
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947441/edit-delete_aoyte5.jpg)
### Home Image
The concert Image is to display that this is a concert booking site. I am the owner of the image.

### sing-in page
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/login_vsgmzr.jpg)
### Sign-up page
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/register_cy1rwb.jpg)

 ### Footer
 A small footer at the end with a youtube link attach to it.

### Navigation bar
The Navigation bar has strong colors that stands out from the calmer base colors that the website has.






## Technology
I used different technologies to make this webpage:

* Coolors
* Balsamiq
* Fontawesome
* Flow chart
* Gitpod
* GitHub
* Heroku
* SQLite
* PostgreSQL
* Git
* Bootstrap 5
* Google Fonts
* Django
* Am I responsive
* VS-code
* Python3
* Git Hub
* cloudinary
* Chrome Dev Tool
* Css Validator
* Html Validator
* Javascript

## Languages

* HTML5
* CSS
## Manuel Testing 
Because of lack of time, I choosed to manually test my website.
### Landing page
* I click on nav button home to check I am navigated to home.
* I check that the hoover effect occur on the home nav button
* I click on the next nav button Login to check I am navigated to the login page.
* I check that the hoover effect occur on the login nav button
* I click on the next nav button register to check that I am navigated to the registration page.
* I check that the hoover effect occur on the register nav button
* I click on the next nav button About to check that I am navigated to the about_booking.html page.
* I check that the hoover effect occur on the about nav button
* I click on the youtube button to check that I am navigated to youtube index page.
* I click on the book button to see if I am restricted to book, because I am not logged in.
* I check that the hoover effect occur on the book button
* I write in the address bar to see if I can navigate to the booking.html page without that I am logged in. I see an error page.
* I write in the address bar to see if I can navigate to the show_booking.html page without that I am logged in. I see an error page.
* I write in the address bar to see if I can navigate to the edit_booking.html page without that I am logged in. I see an error page.
### Register page
* I register in the register page. I check if I can write a username.
* I check if I can write an email in the email input form. I also check if I can write a non email input, I can not.
* I write a password, I check if I can write a different password below, I can not.
* I click the sign up button, to check if it works.
* I check that the hoover effect occur on the sign up button.
* After registration, I check if the navbar names changes: The login button label is now changed to Logout label.
* I check that the hoover effect occur on the logout nav button
* After registration, I check if the navbar names changes: The register button label is now changed to "Your Tickets".
* I check that the hoover effect occur on the "your tickets" nav button.
* I click on book button, to check that I now am navigated to booking.html page.
### Sign in page
* I check if I can write another username and a different password, I can not.
* I click on sign in button with empty inputs, it does not work.
* I write in my username and password, when I click the button, I get logged in.
* I click on sign in button, to check that I now am navigated to home page.
* I check that the hoover effect occur on the "sign in"  button.
### Sign Out page
* I click on sign out button, to check that I now am navigated to home page.
* I click on sign out button, to check that I am signed out
* I check that the hoover effect occur on the "sign out"  button.
### Booking page
* I check that I can choose the summer concert in my booking.
* I check if I can write letters in the ticket input, I can not.
* I check if I can order 0 tickets, I can not. Error message
* I check if I can order 100 tickets, I can not (total amount is 50). Error message occurs
*  I check if I can order 51 tickets, I can not (total amount is 50) Error message occurs
* I check if I can order 50 tickets, I can (total amount is 50). success message
* I click on book button to check if I can book, I can.
* I check that the hoover effect occur on the book button.
* I check that I am navigated to show_booking.html after I have booked, I can.
### Your booking(show_booking.html)
* I check to see if I see information about how many tickets I have booked and for what concert.
* I click on edit button, to see if I am navigated to edit_booking.html page.
* I check that the hoover effect occur on the edit button.
* I click on the delete button, to see if my tickets gets deleted.
* I click on the delete button, to see if I am navigated to home page.
* I click on delete button to see if a success message about my deleted tickets occurs.
* I check that the hoover effect occur on the delete button.
### Edit booking page
* I check if I can choose another concert, I can, it is a selector.
* I check if I can choose another amount of tickets, I can.
* I check if I can book 0 tickets, I can not. Error message occur.
* I check if I can book 100 tickets, I can not. Error message occur.
* I click on update button, to see if it works, it does.
* I check that the hoover effect occur on the update button.
* I click on edit button to see if I am navigated to show_booking.html.
### Admin page
* I check the concert total amount of tickets: Does the tickets decrease when a user book tickets, it does.
* I check the concert total amount of tickets: Does the tickets increase when a user book tickets to a lower amount, it does not.
* I check the concert total amount of tickets: Does the tickets decrease when a user book tickets to a higher amount, it does not.
* I check the concert total amount of tickets: Does the tickets increase when a user delete tickets, it does not.
* I check if I can add new concerts
* I check if I can add new venues.
* I check if only admin can login to admin page.


### Validator Testing 
**HTML**

* The offical W3C validator showed no errors when tested.

**CSS**

* The official Jigsaw validator showed no errors when tested.
**PEP8**
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/pep8_nzj7dl.jpg)


**Accessibility**
* By using lighthouse in devtools I could see that the webpage scored very well on all the tests.
![image](https://res.cloudinary.com/dayrhc7js/image/upload/v1653947440/lighthouse_igerog.jpg)



### Unfixed Bugs
* No unfixed bugs.

## Deployment
It can be wise to deploy to heroku in the very beginning of your project. I will write a step by step from installing django till deployment.
* in terminal write pip3 install 'django<4' gunicorn
* in terminal write: pip3 install dj_database_url psycopg2
* in terminal write: install dj3-cloudinary-storage
* in terminal write: pip3 freeze --local > requirements.txt

* in terminal, django-admin startproject "name" .
* in terminal, python3 manage.py startapp "name"
* Go to settings.py and add "name" in your installed.apps
* in terminal, python3 manage.py migrate
* in terminal, python3 manage.py runserver
* make an env.py file
* Make sure that env.py is included in the gitignore file.
* Add your django password and cloudinary url inside the env.py


* Go into the webpage Heroku.com and create an account.

* In the dashboard in Heroku, click on the "create new app".

* Give your app a unique name and choose your region. Now click on "create app"

* click on resources, add Postgres.


* Go to setting tab and find Config Vars, Click on the "Reveal config Vars" and copy the
 postgres database url.

* In your project, make an env.py file and add postgres database url.

* In Heroku, go to setting tab and find Config Vars. Click on the "Reveal Config Vars".
* In Heroku add PORT as key and value 8000 in config vars
* In Heroku add django secret password in config vars
* In Heroku add cloudinary url in config vars.
* Remember to add cloudinary in installed apps in your project.

* In settings.py find the section about databases and write this:

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

* in terminal, Write python3 manage.py migrate
* Now you are using the heroku database

* In settings.py write this, so you can use herokuapp and localhost. ALLOWED_HOSTS = ['small-venue-booking-app.herokuapp.com', 'localhost']
* You also need to set up your static files in settings.py: write this in settings.py:
 STATIC_URL = '/static/'
 STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
 STATICFILES_DIRS = (os.path.join('static'), )
 STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

 MEDIA_URL = '/media/'
 DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
* You also need to create an template directory in settings.py Write this in settings.py:
  TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Find DIRS in settings.py and add TEMPLATES_DIR
* Now add a Procfile to your project. Inside Procfile, write this: web: gunicorn codevenue.wsgi
* Now you can save, commit deployment and push it to the github if you use that deployment method.

* In heroku, click on Deploy button.
* In heroku Below, click on "Deploy Branch"button.
* Heroku will let you know if the app was successfully deployed.

* Now you can view your app by clicking on the button below the notification.

* You can also choose if the app will rebuild automatically when you do changes and push the code. If you will enable, click "Enable automatic Deploys".




## Credits 
I would like to give my deepest thanks to Get and Shean from code institute.
I would like to thank the slack community that has answered my questions.


## Content

* I got inspired from' I think before I blog' project from code institute: I borrowed the settime js function for the messages:
Here is the original code:


setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

* I also got inspired from the CL love running project to start with this default code to make it easier to use css. Here is the original code from the CL love running project:

*{ margin:0;
padding: 0;
border: none; }

I got inspired from stackoverflow, in how to save a form without including all the users: 
Here is the original code from stackoverflow: https://stackoverflow.com/questions/37773803/saving-modelform-with-user-id


@login_required(login_url='sign_in')
def add_thought(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            return HttpResponse('Hurray, saved!')
    else:
        form = ThoughtForm()
    return render(request, 'lala/add_new_thought.html', {
        'form': form
    })

* I used icons from font awesome

* I used coolors.co to find a nice colour palette to my webpage.

* I used youtube as a social media link.

* I imported a font from google font.
### Media
* I own all the images on the website.


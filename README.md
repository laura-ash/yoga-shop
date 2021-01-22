

# Yoga Time

## Please find the live website [at this link here.](https://yoga-shop.herokuapp.com/)

This project is built all around yoga, which is a much loved hobby of mine. The website will share information on yoga through a blog, and also sell some yoga products. This has been 
a really exciting project for me to do. It was my first time experimenting with Django, which proved to be a really powerful framework with lots of options. Using Django I managed to 
build out the functionality in this website which is discussed below. It was a really cool tool to work with and I really enjoyed this project, I hope you do too!

---


## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
3. [**Information Architecture**](#information-architecture)
    - [**Database Choice**](#database-choice)
    - [**Data Modelling**](#data-modelling)

4. [**Technologies Used**](#technologies-used)
    - [**Languages**](#languages)
    - [**Libraries and Frameworks**](#libraries-and-frameworks)
    - [**Tools**](#tools)
    - [**Databases**](#databases)

5. [**Testing**](#testing)
    - [**Bugs**](#bugs)
6. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Heroku Deployment**](#heroku-deployment)

7. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Content and Media**](#content-and-media)
    - [**Acknowledgements**](#acknowledgements)
8. [**Disclaimer**](#disclaimer)

---

## UX

### Project Goals
#### Visitor/user goals:
- Learn more about yoga
- Purchase yoga products
- Become aware of events 
- Improve their yoga practice

#### Business goals(site owner's goals):
- Make a profit from any purchases on the stories
- Share knowledge of yoga with others
- Create a safe space to learn about yoga
- Promote yoga in Ireland and increase awareness of it's benefits
- Encourage people to try yoga and improve their health
- Promote their yoga products


#### User Stories    
- As a user, I would expect to be able to access the website across all screensizes, from mobile to desktop
- As a user, I would expect be able to navigate the website with ease so I can find what I am looking for with minimal effort
- As a user, I would expect to be able to read information about the business 
- As a user, I would expect be able to learn more about yoga 
- As a user, I would expect be able to see information on events, such as location, cost, date and time
- As a user, I would expect to able to get in touch with the business in case of any further queries
- As a user, I would expect to be able to make a purchase when I want to buy something
- As a user, I would expect to get confirmation of that purchase 
- As a user, I would expect to be able to view and edit my shopping cart  before purchasing
- As a user, I would expect to be able to view a picture and description of items before purchasing
- As a user, I would expect my card details to be safe and secure when I purchase 




### Design

#### General Design Decisions
- The idea behind the overall design of the website was to keep it sleek and modern looking. I decided to go for a minimalist style, which was achieved through using a lot 
of white space and more modern design decisions. This can be seen throughout the website, particularly on the homepage where I was trying to avoid overcrowding too. I wanted 
to prioritize ease of use throughout the whole website design.
- The three gold dots under the headings on the homepage are another example of this minimalist design strategy. They were quite a sleek addition to the homepage, and provided 
a subtle bit of colour to the white space while also maintaining the more modern website design.
- The footer was also designed with the above in mind. Again, there is white space behind the footer instead of a block of colour. This was also implemented to be inline with 
the minimalist strategy, and a simple border top was added to show where the footer started. 
- The above specified design continues onto all of the other pages, including the blog, events, products and shopping bag sections. The more system type pages such as the email 
verification and forgotten password page again echo the same simple but effective design. This was to ensure that all of the page presentations and designs were fully aligned 
in any design decisions.

#### Colours
- I decided to use the colour #a79976 as the primary colour in the website. This provides a nice warm gold blast of colour for the logo and some different 
icons throughout the site too. 
- This was set as the primary colour through CSS variables which means if this ever needs to be changed, it can be done so quickly throughout the site. This 
was a really handy feature, which was great during design. It meant that I could test out different shades of the colour idea I had in mind, and it was just 
one simple change across the website that would handle this. I originally had a more yellow toned colour, but ultimately decided to go with this nice warm 
gold as I thought the site looked nicer with it and there was a better contrast between that and the white space. [More on CSS variables here] 
(https://www.w3schools.com/css/css3_variables.asp), for those looking to learn more about it. 
- As a secondary colour, I went with some light greys which matched warm gold quite nicely. The main one used is #2d2d2d which is mostly applied to 
fonts throughout the website. 

#### Typography
I wanted the fonts that I chose to create a nice design but also be easily readible. For this reason I chose the following;
- Montserrat - A sans-serif font that is used for the body and all main text. It was capitalized for headings and CTAs in some cases which looked quite nice.
- Google Fonts was used to import this font to the project.

#### Icons
Icons were used throughout the project for ease of use. They help grab attention and also highlight what certain parts of the website do, for example the shopping cart is 
represented by a cart icon. These icons we added via FontAwesome. 

### Wireframes
Please see [this link](https://github.com/laura-ash/yoga-shop/tree/master/wireframes) for the wireframes. They were built with Mockflow, which is a online tool to develop wireframes. More information can be found [at this 
link here.](https://www.mockflow.com/
)  
The wireframes contain tablet, mobile and desktop versions. As these were created at the start of the project, there are some 
small aesthetic differences between these and the finished product. This is because small changes were made to adapt to the best design as the project was being built 
out. The wireframes ultimately show that the website is responsive across all screen sizes, which was a priority for this project. Aside from that, they also show the
plan for the website content layout. 

## Features
### Existing Features   
- Users can buy products on the website
- Users can find out about events on the website
- Users can learn more about yoga through the blog
- Users can find out information about the studio and space
- Users can contact the site owners through the contact form 

### Features to Implement in the Future
- Going forward I would love to offer the ability to actually book events through the form 
- It would also be great to add a blog comments section

---
## Information Architecture
### Database choice

While I was in the development phase, I worked with the sqlite3 database which is installed alongside  Django.
Once deployed, a PostgreSQL database is provided by Heroku as an add-on which was used. 

### Data Modelling
#### Products App
##### Product
| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL
 Sku | sku | CharField | max_length=254, null=True, blank=True
 Name | name | CharField | max_length=254 
 Description | description | TextField 
 Price | price | DecimalField |max_digits=6, decimal_places=2
 Image | image| ImageField | null=True, blank=True
 Image Url | image_url | URLField | max_length=1024, null=True, blank=True
 
#### Events App
##### Events
| **Name** | **Database Key** | **Field Type** | **Validation** |
 Name | name | CharField | max_length=120, null=True, blank=True
 Slug | slug | SlugField | null=True, blank=True
 Date | date | DateTimeField | null=True, blank=True
 Facilitator | facilitator | CharField | max_length=140, null=True, blank=True
 Description | description | TextField | null=True, blank=True
 Level | level | CharField | max_length=80, null=True, blank=True
 Image | image | ImageField | null=True, blank=True
 Location | location | CharField | max_length=120, null=True, blank=True

#### Blog App
##### Blog
| **Name** | **Database Key** | **Field Type** | **Validation** |
 Title | title | CharField | max_length=120, null=True, blank=True
 Slug | slug | SlugField | null=True, blank=True 
 Date | date | DateTimeField | auto_now_add=True, null=True, blank=True
 Author | author | CharField | max_length=140, null=True, blank=True
 Body | body | TextField | null=True, blank=True
 Image| image | ImageField | null=True, blank=True

 #### Contact App
 ##### Contacts
 Full Name | full_name | CharField | max_length=50, null=False, blank=False
 Email | email | EmailField | max_length=254, null=False, blank=False
 Message | message | TextField | null=False, blank=False
 Date | date | DateTimeField | auto_now_add=True


## Technologies Used

### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/) 
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) - templating language for Python, to display back-end data in HTML.

### Libraries and Frameworks
- [Django](https://www.djangoproject.com/) - Python framework for building the project.
- [Bootstrap](https://www.bootstrapcdn.com/) - as the front-end framework for layout and design.
- [Google Fonts](https://fonts.google.com/) - to import fonts.
- [FontAwesome](https://fontawesome.com/) - to provide icons used across the project. 
- [Stripe](https://stripe.com/ie) - to handle financial transactions.

### Tools
- [GitPod](https://www.gitpod.io/) - an online IDE for developing this project.
- [Git](https://git-scm.com/) - for version control.
- [GitHub](https://git-scm.com/) - for remotely storing project's code.
- [PIP](https://pip.pypa.io/en/stable/installing/) - for installation of necessary tools.
- [Heroku](https://heroku.com/) - to host the project.

### Databases

## Testing

In order to test this project, I approached the website as a consumer. I also got some family and friends to click through to website to see that everything functioned as expected.
We tested processing orders, reading articles, reaching out through a contact form and all of the other functionality that the app offers.
### Bugs

Problem: When trying to link images in the website, they were not displaying as expected.
Solution: Needed to add "django.template.context_processors.media" under OPTIONS in TEMPLATES in the settings.py file.

Problem: When linking to the checkout page via the secure checkout button in the shopping bag, an error appeared saying that the template was not found.
Solution: After some investigating, I realized the problem was with the folder structure. The checkout.html template was under the following structure; 
checkout > templates > checkout.html. It needed to be changed to checkout > templates > checkout > checkout.html. 

Problem: When integrating Stripe there was an issue with the checkout template. When trying to access it, the error message appeared "AuthenticationError at /checkout/. 
You did not provide an API key."
Solution: In the checkout/views.py there was some code missing. The following needed to be added "'stripe_public_key': stripe_public_key, 'client_secret': intent.client_secret,"

Problem: When setting up Stripe webhooks, it kept returning a 400 error. 
Solution: The server needed to be ended and restarted after exporting the Stripe signing secret. 

Problem: The following error appeared in the terminal window during development "module 'profiles.views' has no attribute 'order_history'". This meant the server could not start.
Solution: After some investigating it turned out the indentation in profiles/views.py was not done correctly. There was an extra indent which led to the function not 
being recognized and this error appearing. 

## Deployment

## Credits

### Acknowledgements     

The code for this project was developed by following the Code Institute video lessons provided for the Boutique Ado Django Mini-Project. However, this was customized and built on 
in order to fit the requirements for this Yoga project. 

Inspiration for the social media icons for the footer taken from Sazzad on codepen, found here - https://codepen.io/sazzad/pen/WbdzzQ/

---

## Disclaimer
This site was made for educational purposes only.        


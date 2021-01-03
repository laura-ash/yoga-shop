

Yoga Time

Please find the live website at this link: 

This project is built all around yoga, which is a much loved hobby of mine. The website will share information on yoga through a blog, and also sell some yoga products.

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
- Create a yoga community where people can share experiences
- Promote yoga in Ireland and increase awareness of it's benefits


#### User Stories    
- Expect to be able to access the website across all screensizes, from mobile to desktop
- Expect to be able to navigate the website with ease so I can find what I am looking for with minimal effort
- Expect to be able to read information about the business 
- Expect to be able to learn more about yoga 
- Expect to be able to see information on events, such as location, cost, date and time
- Expect to be able to get in touch with the business in case of any further queries
- Expect to be able to make a purchase when I want to buy something
- Expect to get confirmation of that purchase 
- Expect to be able to view and edit my shopping cart  before purchasing
- Expect to be able to view a picture and description of items before purchasing
- Expect my card details to be safe and secure when I purchase 




### Design
#### Framework
#### Colours
#### Typography
I wanted the fonts that I chose to create a nice design but also be easily readible. For this reason I chose the following;
- Montserrat - A sans-serif font that is used for the body and all main text. It was capitalized for headings and CTAs in some cases which looked quite nice.
- Google Fonts was used to import this font to the project.

#### Icons
Icons were used throughout the project for ease of use. They help grab attention and also highlight what certain parts of the website do, for example the shopping cart is 
represented by a cart icon. These icons we added via FontAwesome. 

### Wireframes

## Features
### Existing Features   
### Features to Implement in the Future


---
## Information Architecture
### Database choice
### Data Modelling

#### Profile App

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
#### Blog App



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
### Bugs

Problem: When trying to link images in the website, they were not displaying as expected.
Solution: Needed to add "django.template.context_processors.media" under OPTIONS in TEMPLATES in the settings.py file.

Problem: When linking to the checkout page via the secure checkout button in the shopping bag, an error appeared saying that the template was not found.
Solution: After some investigating, I realized the problem was with the folder structure. The checkout.html template was under the following structure; 
checkout > templates > checkout.html. It needed to be changed to checkout > templates > checkout > checkout.html. 

Problem: When integrating Stripe there was an issue with the checkout template. When trying to access it, the error message appeared "AuthenticationError at /checkout/. 
You did not provide an API key."
Solution: In the checkout/views.py there was some code missing. The following needed to be added "'stripe_public_key': stripe_public_key, 'client_secret': intent.client_secret,"

## Deployment

## Credits

### Acknowledgements     
---

## Disclaimer
This site was made for educational purposes only.        


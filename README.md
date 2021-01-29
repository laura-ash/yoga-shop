

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
    - [** Manual Testing **](#manual-testing)
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
- As a user, I would expect to be able to search the products  for what I am looking for 
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
[Google Fonts](https://fonts.google.com/) was used to import custom fonts to the project. I wanted the fonts that I chose to create a nice design but also be easily readible. For this reason I chose the following across the website;
- [Montserrat](https://fonts.google.com/specimen/Montserrat) - This is a sans-serif font that is used for the body and all main text. I chose  this font for a number of reasons. Firstly, 
it is so clear and easy to read which really kept in line with the modern design. Sans-serif fonts would have a much more modern feel to them, which is why it was perfect in this 
website. It is also extremely easy to read which means it's a nicer experience for the customer. 
- I decided to keep this font consistent across the website, and use different styling such as capitalization, colour and letter spacing for different kinds of text such as headings 
and CTAs. 

#### Icons

Icons were used throughout the project for ease of use and to ensure customers could navigate through the website with minimal effort. They help grab attention and also highlight 
what certain parts of the website do, for example the shopping cart is represented by a cart icon. These icons we added via [FontAwesome](https://fontawesome.com/), which is a 
great online library that you can embed in your project and then pull in specific icons. They can be easily styled too which made it great in this case, as I could target them with 
CSS and change their colour and size quite easily. 

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

#### Global features
##### Navigation menu 
- The navigation menu provides an easy way to navigate the site. The following structure can be seen in the navigation menu ;
Products > All Products, Accessories, Clothing
Blog 
Events
Studio
Contact Us 

- The navbar changes to a burger icon on smaller devices, to serve responsive design. The same options as above can be seen when this burger icon is clicked. 
- Bootstrap was used to create this responsive navigation menu. 

##### Footer 
- The footer is also seen across all the website pages. It provides another navigation menu which users can click to bring them to the main site pages. On top of this, it also 
provides information on the company address and links to their social page. Please note that these social links were added for demonstration purposes only, and as the website was 
built for educational purposes they do not lead to live social icons. Should this website be used for a real business though, these links can simply be added to the design once the 
social pages were created. 

#### Main Pages and their Features

##### Products 
- The products page serves the function of showcasing any products that a user wants to potentially purchase. There are some options in the navigation which allow you to focus on different 
product areas too - these would currently be Accessories and Clothing. At the moment, these are the main product categories the yoga shop is selling. This could be builded on with 
more categories if they were added or another business was using this website. 
- If you click on the filter options, you have the ability to switch within the actual page between Accessories and Clothing. 
- There is also an option to sort in the top right of the page, which allows users to put the products in order of price or category. 
- Each product also is tagged with it's product category, which we can see denoted by a FontAwesome icon in the description box of each product. 
- There is also the option to "View More" on each product, which brings the user to that individual product detail page. 
- On that product detail page, the user has the ability to read the full product description. 
- If they decide to purchase the product, they can select "Add to Bag" and specify the quantity also they would like to add to. 

##### Shopping cart
- The user has the option to click shopping bag in the top right of the website too. 
- This will store any items they have added to their cart.
- Here they can also increase or reduce the quantity of the product in the bag, or remove the product completely from the bag if they wish. 
- They can also see the monetary value of their shopping cart from this screen, or if they look at the shopping bag icon on the top of each page. 
- The user can also see how much their shipping is from this screen, and how much more money they need to spend to qualify for free shipping 
(if they haven't already). 

##### Blog 
- The blog page shows all of the different blogs that the site owner has published. 
- It shows the date of each article published, and an intro into the article content. 
- These blog posts are ordered by the most recently publish being first. 
- Users can click into them and read more for any articles they are interested in. 

##### Events 
- The events page shows all of the upcoming events in the studio.
- These are also ordered by the ones closest to todays date. 
- Information on the date, facilitator and level of yoga recommended are included on each event card.

##### Studio 
- The studio page provides information on the yoga space itself. 
- It serves as an informational page. 

##### Contact Us
- The contact us page allows for site visitors to get in touch with the site owners.
- Once the form is submitted, the user details are recorded included their name, email and message.
- If you are an authenticated superuser, there is also the possibility to go to the form submissions page and check the recent form submissions.
- This provides a place that the site owners can see who has reached out to them and allows them to get in touch with them accordingly. 



### Features to Implement in the Future
- Going forward I would love to offer the ability to actually book events through the form.
- It would also be great to add a blog comments section.

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
--- | --- | --- | --- 
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
--- | --- | --- | --- 
 Title | title | CharField | max_length=120, null=True, blank=True
 Slug | slug | SlugField | null=True, blank=True 
 Date | date | DateTimeField | auto_now_add=True, null=True, blank=True
 Author | author | CharField | max_length=140, null=True, blank=True
 Body | body | TextField | null=True, blank=True
 Image| image | ImageField | null=True, blank=True

 #### Contact App
 ##### Contacts
 | **Name** | **Database Key** | **Field Type** | **Validation** |
 --- | --- | --- | --- 
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

### Manual Testing
The first step in the testing journey was manual testing, where I went through each feature on a range of screen sizes, browsers and devices. The aim here was to ensure that 
everything on the frontend was working for users and provided a responsive and easily navigable design. I also checked these across each of the user stories to be sure 
these were each addressed. Overall, I approached the website as a consumer. I also got some family and friends to click through to website to see that everything functioned as expected.
We tested processing orders, reading articles, reaching out through a contact form and all of the other functionality that the app offers. See details of this manual testing 
and the user stories each step corresponds to below.

#### Responsiveness: 
User stories: 
- As a user, I would expect to be able to access the website across all screen sizes, from mobile to desktop

Steps: 
- I went through each page of the website using the Google Chrome Dev tools. This allowed me to use the multi screen testing option, and I could view the website from a range of different screen sizes.

#### Navigation:
User stories:
- As a user, I would expect be able to navigate the website with ease so I can find what I am looking for with minimal effort
Steps: 
- To test this, I clicked into every link in the nav bar to be sure they were all connected properly. Within the pages, I ensured that all of the CTAs, buttons, and links were connected properly too. 

#### Content: 
User stories:
- As a user, I would expect to be able to read information about the business 
- As a user, I would expect be able to learn more about yoga 
- As a user, I would expect be able to see information on events, such as location, cost, date and time

Steps: 
- These stories were mainly addressed with the blog and events features.
- To test this, I went through each of the blog posts and events to make sure everything was working as expected. 

#### Contact: 
User stories:
- As a user, I would expect to able to get in touch with the business in case of any further queries

Steps: 
- To test this, I submitted the contact form to be sure that my submission was registering. 

#### Functions:
User stories:
- As a user, I would expect to be able to make a purchase when I want to buy something
- As a user, I would expect to get confirmation of that purchase 
- As a user, I would expect to be able to view and edit my shopping cart  before purchasing
- As a user, I would expect to be able to view a picture and description of items before purchasing
- As a user, I would expect my card details to be safe and secure when I purchase 

Steps: 
- These stories would refer to the purchasing option from the products page.
- In order to test this, I attempted to purchase different items from the products page.
- I checked that the amount was increasing and decreasing as products were added to the bag, and similar with the product quantities being updated.
- When we got to the payment screen, I then used the Stripe demo cards to test purchase going through. 

#### Search: 
User stories:
- As a user, I would expect to be able to search the products  for what I am looking for 

Steps: 
- In order to test this, I conducted different searches using the search bar. I then checked against the search keywords and the search results that everything was behaving as expected.

### Bugs

#### 1. Broken images on website
**Problem:** When trying to link images in the website, they were not displaying as expected.

**Solution:** Needed to add "django.template.context_processors.media" under OPTIONS in TEMPLATES in the settings.py file.

#### 2. Template could not be found 
**Problem:** When linking to the checkout page via the secure checkout button in the shopping bag, an error appeared saying that the template was not found.

**Solution:** After some investigating, I realized the problem was with the folder structure. The checkout.html template was under the following structure; 
checkout > templates > checkout.html. It needed to be changed to checkout > templates > checkout > checkout.html. 

#### 3. Authentication error with Stripe
**Problem:** When integrating Stripe there was an issue with the checkout template. When trying to access it, the error message appeared "AuthenticationError at /checkout/. 
You did not provide an API key."

**Solution:** In the checkout/views.py there was some code missing. The following needed to be added "'stripe_public_key': stripe_public_key, 'client_secret': intent.client_secret,"

#### 4. 404 error with Stripe webhooks
**Problem:** When setting up Stripe webhooks, it kept returning a 400 error. 

**Solution:** The server needed to be ended and restarted after exporting the Stripe signing secret. 

#### 5. Missing attribute for order template
**Problem:** The following error appeared in the terminal window during development "module 'profiles.views' has no attribute 'order_history'". This meant the server could not start.

**Solution:** After some investigating it turned out the indentation in profiles/views.py was not done correctly. There was an extra indent which led to the function not 
being recognized and this error appearing. 

## Deployment
### Local Deployment

To run this project locally, you must install the following tools;
- IDE - you can use whichever you like. I used [GitPod](https://www.gitpod.io/) when creating this project. 
- [Git](https://git-scm.com/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python3](https://www.python.org/download/releases/3.0/)

On top of this, you will need to create accounts with these services. You can sign up for all of these online at the attached links;
- [Stripe](https://stripe.com/en-ie) to handle the payments
- [Gmail](https://mail.google.com/) to set up the emails from, such as to verify a new user email

Instructions
- Clone this repo into your chosen code editor. You can do this via the terminal window or by downloading it from GitHub. There is a great article on the GitHub Help page which goes further into this process. 
- You must now add your environment variables. You can follow these steps;
-- Create a .env file in the root directory.
-- Add the .env file to the .gitignore file in your project's root directory. This means your environment variables will not be in version control. This is an important step for security purposes. 
-- Within the .env file set your  environment variables as follows; 
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret key>"    
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH_Secret key>"   
```

- Now you must add these requirements from the requirements.txt file, by typing the following command in the terminal;
`pip3 install -r requirements.txt`
- Next step is to create the database. Migrate the models to connect the database by typing the following commands In the terminal: 
`python3 manage.py makemigrations`
`python3 manage.py migrate`
- Create a superuser within the account so you can access the admin panel. Put the following command in the terminal and follow the prompts; then and insert username,email and password):
`python3 manage.py createsuperuser`
- You should now be able to run the application by typing the following command in the terminal:
`python3 manage.py runserver`

### Heroku Deployment 

In order to deploy to Heroku, I had first had the project locally deployed. I took the following steps;
- Created a requirements.txt file, by adding the following command to the terminal; `pip3 freeze > requirements.txt`. This was to tell Heroku what dependencies needed to be installed to successfully deploy. 
- Created a Procfile with the following command `web: gunicorn art_of_tea.wsgi:application`. This tells Heroku how to run the project. 
- Used the following commands to push to GitHub; `git add`, `git commit` and `git push` 
- Created an account with AWS and set up a  AWS S3 Bucket in order to host the static files. I added my static files here, including css and media.
- Created a new app within Heroku.
- Under the Resources tab in Heroku, I searched for Heroku Postgres, selectedHobby Dev — Free and then clicked Provision. This added the resource to the project.
- Under the Heroku Settings tab, I navigated to “Reveal Config Vars”
- With the Config Vars, I added the following  keys with the aim of also adding their corresponding values which I would get from AWS, Stripe and Gmail; 

````
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
SECRET_KEY
STRIPE_PUBLIC_KEY 
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
USE_AWS
````

- After this I migrated the database models to the Postgres database using the following commands in the terminal:
python3 manage.py makemigrations
python3 manage.py migrate
- I then created a superuser by following this command here `python3 manage.py`
- I added the Heroku app URL to ALLOWED_HOSTS under settings.py. 
- I also connected GitHub to Heroku so it would update and deploy with each push to GitHub. 
- To set up the sending of real emails, I created a Gmail account. I then added these details to the EMAIL_HOST_USER variable and the app password generated by Gmail 
in the EMAIL_HOST_PASS variable.
- The application was then successfully deployed on a URL provided by Heroku. 


## Credits

### Acknowledgements     

The code for this project was developed by following the Code Institute video lessons provided for the Boutique Ado Django Mini-Project. However, this was customized and built on 
in order to fit the requirements for this Yoga project. 

Inspiration for the social media icons for the footer taken from Sazzad on codepen, found here - https://codepen.io/sazzad/pen/WbdzzQ/

---

## Disclaimer
This site was made for educational purposes only.        


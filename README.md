# Munch

Munch is a social recipe blog website where users (Munchers) come together to share recipes with other users. As a user you can add, edit, delete, comment and like recipes.

The live link can be found here - [Munch]()

![responsive]()

## User Experience (UX)

Munch is a website for all ages but specifically tailored to adults where they can explore different recipes and cuisines or share their own in a community of foodies also known as Munchers!

## User Stories 

### EPIC | Navigation
- As a User I can navigate around the site so that I can easily view desired content.
- As a User I can view a list of recipes so that I can select one to read.
- As a User I can select a recipe so that I can read the recipe details
- As a User I can search for recipes so that I can find specific recipes.

### EPIC | User's Recipes
- As a User I can create a recipe so that other Munch users can view them.
- As a User I can edit recipes so that I can update any changes or mistakes to my recipes.
- As a User I can delete recipes so that I can remove any submitted recipes.

### EPIC | User Interaction
- As a User I can like/unlike recipes so that I can mark my favourite recipes
- As a User I can view the number of likes on a recipe so that I can see which is most popular.
- As a User I can leave comments on a recipe so that I give feedback and opinions and feel involved in the conversation
- As a User I can view comments on recipes so that I can read other user's comments and be part of the conversation.

### EPIC | Sign in
- As a User I can register an account so that I can like/dislike, comment and upload recipes.
- As a User I can log in and out of my account so that I can control and manage my account

### EPIC | Admin
- As an Admin I can view, create, edit and delete all recipes and comments so that I can control the website's content.

## Design

The design of the app is based on the wireframes with a mix of another food blog called [iamafoodblog](https://iamafoodblog.com/) and Code Institutes 'I think therefore I Blog' project.   

### Colour Scheme
- The colour scheme for Munch is fairly simple, minimal and aesthetically pleasing. I used a very dark grey, white and some subtle hints of colour such as the red/maroon buttons to contrast the hero image on the home page. I went for this style as it is clean but also because it is versatile as it matches with most colours which is important as the site would complement the colours of the images uploaded by users, and keep the recipes the center of attention.

### Typography
- The font used on Munch is Dosis as it is a clear and easily readable font. It is also a unique and fun font which goes with the blog theme of the site.  

### Imagery
- All the images are based on food and where taken from this [site.](https://iamafoodblog.com/)

## Database Schema 

The design of the database can be seen below.

![Database Schema](/static/images/Munch-ERD.png)

## Features

### Home Page

### Navigation bar
- The navigation bar is at the top of every page and contains the links to all the other pages.
- The current page is highlighted active to the user by bolder font. 
- Hovering over the nav links will brighten the font.
- The links to "Register" and "Log in" will change to "Log Out" once the user has logged in to their account.
- Once a user has logged in, more links will be displayed. The links that will be displayed are "Profile" which is a dropdown box which contains two options which are "Add Recipe" and "Liked Recipes".
- There is a search bar on the right side of the navbar so users can easily and quickly search for recipes.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size is small e.g. mobile. 

![Navbar](/static/images/Munch-navbar.png)

### Hero Image
- The hero image welcomes the user with the Munch catch line and tells the user to sign up to start Munching.
- There is a sign up button just below the message. Clicking the button will take the user to the register page.
- When a user is signed in the message changes to "Lets start Munching {Username}" and the sign up button changes to the recipes button which once clicked on takes the user to the recipes page. 

![Hero Image](/static/images/Hero-1.png)

![Hero Image Logged In](/static/images/Hero-2.png)

### About Us
- The about us section explains to the user a bit about the Munch website.
- It also shows the user that we cultivate an inclusive community.

![About Us](/static/images/about-us.png)

### Features
- The features section displays three short messages stating some functionality of the Munch website next to images of food.

![features](static/images/features.png)



# **PP4 - House Ukraine In Ireland**

## **Summary:**
House Ukraine In Ireland is an network designed around helping those fleeing from Ukraine to Ireland with finding accommodation. The site is designed to assist both those seeking accommodation and those providing accommodation. The site features information about the Irish Government's Accommodation Recognition Payment Scheme and how they can apply for it. It also allows it's users to post to the site stating if they are seeking or providing accommodation in order assist them with finding what they require.

***

## **Table of Contents**

+ [User Experience](#user-experience)
+ [Features](#features)
+ [Design](#design)
+ [Planning](#planning)
+ [Technologies Used](#technologies-used)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)
+ [Acknowledgements](#acknowledgments)

***

## **User Experience**

### **Project Goals:**
My main goal for this project was to design and create a fully functional blog-like django site. The site would have full CRUD functionality allowing registered users to Create, Read, Update & Delete blog posts and comments made by them. A registered user should have full control over there own posts with a superuser also being present to ensure all posts/comments are being made with good intentions.


***

## **Features**

### **Implemented Features:**
- __Feature 01 Navigation Bar__

The navigation bar has a simplistic and consistent style allowing users to easily navigate the pages. It includes a text logo which I have styled to have both the Ukrainian & Irish national flag colours. A "Stand With Ukraine" banner has been added which features a link to the [Stand With Ukraine](https://www.standwithukraine.how/) Website which has information in regards to how people can support the Ukrainian people. The nav page links are "Home" which displays the home page where users can find posts made by users in regards to those seeking or providing accommodation in Ireland, the "About" page which features information in regards to the sites purpose as well as linking information to government websites which provide information about the accommodation recognition payment, the "Login" & "Register" pages which allows users to sign in or create an account in order to create posts and leave comments on posts made and finally the "Logout" page which is only displayed once users create an account and are actively sign-in.

![Navbar Signed-Out](/media/images/nav-bar-signed-out.PNG)
![Navbar Signed-In](/media/images/nav-bar-signed-in.PNG)
![Navbar Mobile](/media/images/nav-bar-mobile.PNG)


- __Feature 02 Landing Page__

The Landing page features the blog posts users have made in regards to accommodation being sought or provided. The posts are displayed evenly with 2 rows consisting of 3 posts for a max of 6 posts per page. The posts themselves feature an image, post author, title, description, time posted and a like counter.

![Landing Page](/media/images/landing-page.PNG)


- __Feature 03 Post Detail Page__

Each post made can be selected which brings the user to the post's detail page. This features the posts full details where users can outline what it is they are providing/seeking. Common information given includes accommodation location, available period and contact information for those providing accommodation. While information about the user, there family, current accommodation status and contact information is usually given by those seeking accommodation.

![Post Detail Page](/media/images/post-detail-page.PNG)


- __Feature 04 User Authentication/Registration__

In order for site users to avail of certain features on the site they must sign in. A user needs to be registered before signing in. This can be done via the Register Nav Bar link in order to register users must create a username, then a password this must be entered twice, an email can also be given however this is optional.

![Register Page](/media/images/sign-up.PNG)

Once users have register they will automatically be logged in to that account however, should the user leave the site and come back to find themselves logged out then they should navigate to the login page found on the navbar. Here they can enter the username and password they used when registering to sign back in.

![Sign-In Page](/media/images/log-in.PNG)

Should a user for any reason want to sign out of there current account they can do so by navigating to the Logout navbar link this is only displayed when users are logged-in and it replaces the register and login navbar links as a result.

![Sign-Out Page](/media/images/sign-out.PNG)


- __Feature 05 Comment on a Post__

Once a user has created an account and signed in they will be given the ability to make comments on posts. This allows users to interact with the user who created the post in order to enquire in regards to information or to simply interact with other users who have also commented on the post.

![Post Comments](/media/images/post-comments.PNG)

Comments have to be approved by a superuser in order to be displayed. This is to ensure that all comments are being made with good intention and to prevent hate speech from being spread on the site. Once a user submits a comment a notification will be displayed informing the user that there comment is awaiting approval.

![Comment Approval](/media/images/comment-approval.PNG)


- __Feature 06 Like a Post__

Users that are signed in have the ability to like posts. This can be done by simply clicking on a post to enter its post details page. Once there users will find a heart and air bubbles icon in the bottom left of the posts content section. The heart represents the number of likes a post has received and the air bubbles represent the number of comments.

![Unliked Post](/media/images/unliked-post.PNG)

To like the post users simply have to click on the heart icon and the page will automatically reload to show the new number of likes that a post has received.

![Liked Post](/media/images/liked-post.PNG)


- __Feature 07 Create User Posts__

Once a user has created an account and signed in they will be given the ability to create posts. The create post icon can be found just below the navbar on the home page.

![Create Post Icon](/media/images/home-create-post.PNG)

Once selected the user will be brought to the post-user page where they can input the title of there post, the content where they can input information about what accommodation they are providing or information about themselves if they are seeking accommodation. Finally users can input an image they would like to display to other users in regards to their post. If no image is given a default placeholder image will be used instead.

![Post Creation](/media/images/create-post.PNG)

Just like comments posts must be approved by an admin/superuser before they can be displayed on the site for other users to see. This is to ensure all posts created are being made with good intention and that they are legitimate posts from people genuinely seeking or providing accommodation.

![Post Approval](/media/images/post-approval.PNG)


- __Feature 08 Edit User Posts__

Once a user has created a post they can edit it by navigating too the Edit Posts Page. This can be found by clicking the Edit Post Icon on the landing page.

![Post Edit](/media/images/home-create-post.PNG)

Once selected the user will be displayed with a list of all the posts that they have created on the site and can choose to edit a post by selecting it from the menu.

![Select Post to Edit](/media/images/Edit%20Posts.PNG)

- __Feature 09 SuperUser Approval/Monitoring__

To ensure a safe a properly functioning site user features such as comments & posts have to be approved by a superuser. This can be done by navigating to the django admin panel by adding /admin to the end of home page url. Once logged in the superuser can create, edit, approve and delete posts and comments made by themselves or other users. This is done to ensure spam, hate speech or potential scams are not displayed to other users on the site. 

![Admin Post Menu](/media/images/admin-post.PNG)
![Admin Comment Menu](/media/images/admin-comment.PNG)


### **Non-Implemented Features**
Due to project time constraints not all desired features can be implemented, however this is quite normal in the development of any software related product. This is why it is crucial to ensure Agile Based Principals are followed when making any software related product to ensure that essential features are priortised over less-essential features. That being said there are still a number of features which could potentially be implemented in the future to add better value and overall functionality to the site. Listed below are just a few:

- __Customisable Profile Page__

To allow users to better describe who they are and what it is they are providing or seeking a customisable profile page who be a good feature to implement. This would allow users to add more of personal touch to their accounts and allow them to list details such as who they are, there current occupation, contact information and general bio information such as their name, age etc.


- __Private Messaging Channel__

Some users may want to speak to other users directly but don't want to contact them via email or phone. A private messaging channel similar to that seen on social media sites such as twitter and facebook would be a desirable feature to add to this project. It would create a new layer of functionality to the site and make it easier for users to ask more personal questions rather then leaving comments which can be seen by any other user if they simply click into a post and read the comments section.


## **Design**

### **Wireframes**

Before starting my project I designed some basic wireframe mockups I did this in order to give me a better feel for the overall desired look of how I wanted to my site to appear to users.

- __Mockup 1: Landing Page__

![Landing Page](/media/images/landing-page-mockup.PNG)


- __Mockup 2: Post Detail Page__

![Post Detail Page](/media/images/post-detail-page-mockup.PNG)


### **Site Map**

This is a diagram of how the site functions and how a user can access each function:

![Site Map](/media/images/site-map.PNG)


### **Data Model**

- __Entity Relation Diagram - Post__

![ERD Post](/media/images/ERD-Post.PNG)


- __Entity Relation Diagram - Comment__

![ERD Comment](/media/images/ERD-Comment.PNG)


## **Planning**

### **Planning/Strategy:**
Before beginning my project an Agile methodology was used to plan out my projects intended purpose/features. I done this by creating a project called CalumRiot's PP4 in this I created a product backlog using the principals of Agile to assign each possible feature a User Story and a priority using the MoSCoW prioritisation method. In total I had 6 Must-Haves, 5 Should-Haves, 2 Could-Haves & 3 Won't Haves.
This Project Backlog can be viewed here: [CalumRiot's PP4](https://github.com/users/CalumRiot/projects/6/views/1)


## **Technologies Used**

### **Languages Used**
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [JQuery](https://en.wikipedia.org/wiki/JQuery)

### **Frameworks, Programs & Libraries Used**
- [Font Awesome:](https://fontawesome.com/) Was used to add icons to give an aesthetic design to my social media links.
- [Git:](https://en.wikipedia.org/wiki/Git) Was utilised for my Gitpod Terminal in order to add, commit and push changes made to my code to GitHub.
- [GitHub:](https://en.wikipedia.org/wiki/GitHub) It is used as a repository for my projects code with code being pushed to GitHub via Git. My Product Backlog was also designed in GitHub's Projects.
- [LucidChart:](https://en.wikipedia.org/wiki/Lucidchart) Was used to design my Mockups, Site Map & Enitity Relationship Diagrams.
- [Django:](https://en.wikipedia.org/wiki/Django_(web_framework)) Was used as a framework to support the quick and secure development of this project.
- [BootStrap:](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)) Was used to help build a responsive website more easily.
- [Bootswatch:](https://bootswatch.com/) Was used to give my bootstrap a customised theme to help improve UX and the sites aesthetic.
- [Gunicorn](https://gunicorn.org/) Was used as the Web Server to run Django on Heroku.
- [dj_database_url](https://pypi.org/project/dj-database-url/) Is the library used to allow database urls to connect to the postgres db.
- [psycopg2](https://pypi.org/project/psycopg2/) Is the database adapter used to support the connection to the postgres db.
- [Cloudinary](https://cloudinary.com/) Was used to store the images used for the project.
- [Summernote](https://pypi.org/project/django-summernote/) Was used to provide WYSIWYG editing for the admin create post panel.
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) Was used for account registration and authentication.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Was used to assist in simplifing form rendering.
- [Jquery Library](https://en.wikipedia.org/wiki/JQuery) Was used to fade out alert messages.

## **Testing**

### **Browser Testing**

I performed tests on various browsers to ensure that my site was cross-browser compatible. The browsers which I performed the tests on where:
- Google Chrome Version: 111.0.5563.146
- Firefox Browser Version: 110.0.1
- Microsoft Edge Version: 111.0. 1661.41

### **Responsiveness**

I performed responsiveness tests using Chrome Developer Tools to test responsiveness on a range of monitor sizes including ultra wide 5k screens (5120 x 2880 px) and smaller width devices such as the IPhone SE (375 x 667 px).

### **Validator Testing**

**W3C Markup Validator:**

I performed validator testing using [W3C Validator](https://validator.w3.org/) due too the django html tags I was receiving errors on my html code therefore I had to manually remove the tags to ensure they where validated correctly.

![Landing Page Validation](/media/images/landing-page-validator.PNG)

I received errors on my other html pages due too no head or no defined html tags at the start of each html file this is due too each html page being extended from the base.html file therefore these tags are not required and the errors can be ignored.

![About Page Validation](/media/images/about-page-validator.PNG)

**PEP8 CI Testing**

I performed validator testing using [CI Python Linter](https://pep8ci.herokuapp.com/#) which is Code Institute's PEP8 Python Tester. After performing tests on each python file I received only whitespace and line too long errors which due to the fact that these errors do not actually affect the code I simply ignored.

![Admin-py Validation](/media/images/admin-py-validator.PNG)

![Models-py Validation](/media/images/models-py-validator.PNG)

![Views-py Validation](/media/images/views-py-validator.PNG)

![Urls-py Validation](/media/images/urls-py-validator.PNG)

![Forms-py Validation](/media/images/forms-py-validator.PNG)

### **Lighthouse Testing**

Lighthouse Testing was performed on the site using Google Chrome Dev Tools. A test for both Desktop & Mobile Devices was performed.

**Desktop Test**

![Desktop Lighthouse Test](/media/images/desktop-lighthouse.PNG)

**Mobile Test**

![Mobile Lighthouse Test](/media/images/mobile-lighthouse.PNG)

### **PyTest**

I created 3 test files to test my models, views and forms.py files. I then used Pytest to run these test to see if they passed or failed. The test files are:

- [test_models](/blog/test_models.py)
- [test_views](/blog/test_views.py)
- [test_forms](/blog/test_forms.py)

### **Known Bugs**

- The Edit Post Function is able to display all posts created by the user. However when attempting to edit the post and save the changes an error message will occur. The only solution to this issue at the moment is to edit user posts via the django admin panel.



## **Deployment**
The Project is deployed to Heroku with the following steps being taken to deploy it:
- Login to the [Heroku](https://id.heroku.com/login) Dashboard to access the created apps menu.
- Select new followed by create new app.
- Create a custom name for your app and select your current region.
- Select Create New App.
- Navigate to the Settings tab and select Reveal Config Vars.
- Before completing the next 3 steps ensure you have correctly configured your DATABASE_URL & SECRET_KEY in your settings.py file storing both of these vars in your env.py for security.
- Add a new config var called DATABASE_URL with an input of the url link.
- Add a new config var called DISABLE_COLLECTSTATIC with an input of 1.
- Add a new config var called SECRET_KEY with an input of the secret key you used in your env.py file.
- Navigate to the Deploy tab and ensure your deployment method is connected to your project's GitHub Repo.
- Ensure you have pushed your most recent project version to your GitHub Repo.
- Ensure you have a Procfile with the following code "web: gunicorn 'projectname'.wsgi".
- Finally select deploy branch from main at the bottom of the deploy tab.


## **Credits**

- None of the photos listed on the site are mine all have been taken from various news pages for the educational purpose of demonstrating this project.
- Parts of my models and views.py files have been from the CI: I think therefore I Blog Sample Walkthrough Project


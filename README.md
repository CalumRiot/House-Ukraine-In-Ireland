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

### **Planning/Strategy:**
Before beginning my project an Agile methodology was used to plan out my projects intended purpose/features. I done this by creating a project called CalumRiot's PP4 in this I created a product backlog using the principals of Agile to assign each possible feature a User Story and a priority using the MoSCoW prioritisation method. In total I had 6 Must-Haves, 5 Should-Haves, 2 Could-Haves & 3 Won't Haves.
This Project Backlog can be viewed here: [CalumRiot's PP4](https://github.com/users/CalumRiot/projects/6/views/1)

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


- __Feature 08 SuperUser Approval/Monitoring__

To ensure a safe a properly functioning site user features such as comments & posts have to be approved by a superuser. This can be done by navigating to the django admin panel by adding /admin to the end of home page url. Once logged in the superuser can create, edit, approve and delete posts and comments made by themselves or other users. This is done to ensure spam, hate speech or potential scams are not displayed to other users on the site. 

![Admin Post Menu](/media/images/admin-post.PNG)
![Admin Comment Menu](/media/images/admin-comment.PNG)

## **Design**



## **Planning**



## **Technologies Used**



## **Testing**



## **Deployment**



## **Credits**



## **Acknowledgments**
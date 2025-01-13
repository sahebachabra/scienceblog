# ReadMe
{% load static %}
To do



- [ ] Like unlike function
- [ ] Should do must do
- [ ] Read me
- [ ] Testing
- [ ] You’ve added a post page
- [ ] Front end stuff

ER Diagram



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")




*  Pick tag or category 
* @is_superuser
* Peer review 

Wireframe



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")




<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")



# **Neuroscience Blog Website**

<img src="{% static 'responsive.png' %}" alt="Responsive design mockup">

## **Overview**


### **Purpose**

This project is a blog website aimed at individuals interested in neuroscience, including students, professors, and academics. The goal is to create an engaging platform for users to share, discuss, and learn about neuroscience through blog posts, likes, and other interactions. The site provides an opportunity for users to contribute their knowledge, engage with community discussions, and learn from peers in the field.


### **Target Audience**

The website is targeted at those who are curious about neuroscience, including high school students, university students and professors 


## **User Stories**


### **Must-Have User Stories**

As a registered user, \
I want to create and publish blog posts related to neuroscience, \
so that I can share my knowledge with the community.

Acceptance Criteria:



* Logged-in users should see a "Create Post" button on their dashboard.
* Users must provide a title, content, and select at least one category (e.g., Cognitive Neuroscience).
* Users can optionally add tags and upload a featured image.
* Posts are saved as drafts by default and require explicit action to publish.
* Only published posts appear on the homepage.

As a neuroscience enthusiast (student or academic), \
I want to create an account on the blog, \
so that I can contribute posts, comment, and engage with other users.

Acceptance Criteria:



* Users can navigate to the registration page from the homepage.
* Users must provide a username, email, and password.
* Passwords must meet security requirements (e.g., minimum 8 characters, at least one number).
* The system should send a confirmation email after registration.
* Users should be redirected to the homepage upon successful registration.

As a logged-in user, \
I want to be able to like and unlike on blog posts, \
so that I can engage with the author and other readers.

Acceptance Criteria:



* A like count should appear below each post for logged-in users.
* They should be able to like the post, increasing the like count


### **Should-Have User Stories**

As a neuroscience student, \
I want to filter posts by specific categories or tags, \
so that I can find relevant content more easily.

Acceptance Criteria:



* Categories should appear as a dropdown menu in the navigation bar.
* Tags should be displayed as clickable links on each post.
* Clicking a category or tag should filter posts to only display relevant ones.
* Pagination should work correctly when filtering by category or tag.


### **Could-Have User Stories**

As a neuroscience academic, \
I want to view profiles of other contributors, \
so that I can learn about their expertise and interests.

Acceptance Criteria:



* Clicking a user’s name on a post or comment redirects to their profile page.
* Profiles should display the user’s username, bio, and list of posts they’ve authored.
* Users can optionally share their academic affiliation and research interests.
* Profiles should not display sensitive data (e.g., email addresses).


## **Design Decisions**


### **Wireframes**



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")




<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")



### **Accessibility Considerations **



* High contrast between text and background for readability.
* Alt text for images to ensure accessibility for visually impaired users.
* Resizable text to maintain legibility on mobile devices and smaller screens.


## **AI Tools Usage**

I used ChatGPT a few time to try and fix minor bugs and also I wanted to make some interesting spooky effects so I used to it help me make a .sectionimagehover in my css


### **GitHub Copilot**

I did not use GitHub Copilot


## **Features Implementation**


### **Core Features (Must-Haves)**



* **Post Creation**: Users can create, edit, and publish blog posts on neuroscience topics..
* **Like System**: Users can like posts to express appreciation.


### **Advanced Features (Should-Haves)**



* **Categories and Tags**: Posts can be filtered by categories or tags for easier navigation.
* **User Profiles**: Users can view others' profiles, including their posts and academic affiliations.


### **Optional Features (Could-Haves)**



* **Post Filtering by Author**: Users can filter posts by author to explore content by specific contributors.
* **Follow System**: Users can follow other users to receive updates on their posts and activities.
* 


## **Testing and Validation**


### **Testing Results**

The website was tested across different devices and screen sizes using Chrome DevTools. It performed well on desktops, tablets, and mobile phones. Adjustments were made to improve layout responsiveness and prevent text from touching the screen edges on mobile devices.


### **Validation**

Minor errors were identified after deployment and issues with visuals on phones were identified using google extension.


## **Deployment**


### **Deployment Process**

The website is hosted on Heroku and deployed with a PostgreSQL database. Some challenges with image display on the site were resolved by fixing relative links in the HTML.


## **Reflection on Development Process**


### **Successes**



* Effective use of Code Institute staff and AI tools, significantly streamlined the development process (but not using it too much)
* The final design achieved the right balance between being fun and informative


### **Challenges**



* Some CSS commands conflicted, causing styling issues.
* Accessibility adjustments, especially for mobile responsiveness, were more complex than expected.
* 
* Some accessibility adjustments were more complex than anticipated, especiallly adjusting image size to phones and tablets


### **Final Thoughts**

This project provided valuable insights into creating an engaging blog website, balancing design with functionality, and ensuring accessibility. The experience has honed my ability to build user-centric platforms while maintaining academic professionalism.


## **Code Attribution**

All code was written by me


## **Future Improvements**



* Implementing an interactive quiz or checklist feature for parents to assess their readiness for Halloween.
* Add links to pdfs of fire safety and allergies
* Adding a blog section for ongoing seasonal safety tips.
* Further testing and optimization for older devices and browsers.
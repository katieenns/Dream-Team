# How to run the application

## Environment to run the application

- Python 3.10.7
- Pip 22.2.2

## Steps to run the application

1. Clone the entire project source code from github by running command below in command prompt. Make sure `git` is installed on your local machine.

    `git clone https://github.com/katieenns/Dream-Team.git`
    
2. In command prompt, access the the directory "Dream-Team"

   `cd Dream-Team`

3. Create Virtual Environment

    Install virtual environment:

    `pip install virtualenv`

    Create virtual environment named "webappenv" (Note : In command prompt make sure you are accessing same root folder where you have cloned source code in step 1)

    `python -m virtualenv webappenv`
    
4. Activate the virtual environment:

    For Windows OS use command below
    
     `webappenv\Scripts\activate`

    For Mac and other Linux OS use command below.
    
    `source webappenv/bin/activate`
    
5. Install the packages you need from requirements.txt. To install, use the commamd below.

    `(webappenv)$ pip install -r requirements.txt`
    

6. Run the server on your machine

    `(webappenv)$ python main.py`

    The website can be accessed at `http://127.0.0.1:5000`

# YELP's Search API Explorer

## PART A
### Concept
A responsive web-based GIS application with python and consuming Yelp’s search API, to re-represent their data into a new / better user-interface that includes an interactive geographical window with an accompanying window for filtering searches in the categories of ((Active Life, Arts & Entertainment, Beauty and Leisure, Bicycles, Food & Drink, ~Health & Medical; aka Feature-Type), (and subcategories ~Rating,~Distance from defined location)). The GUI will allow users to click and toggle the ‘displayed features’ of the map (restaurants, parks, etc.) to see additional information about that feature, including how far it is from the user defined location.

### Team Members
Katie Enns, Hunter Sayre, Javier Aguilar, and Pankaj Chaudhari

### Team Name
Dream Team

### Stakeholders
Relevant stakeholders include Local Businesses, Claremont College Students, and Local cities within US.

### User Stories (estimate of completion times) and Development Priorities
1. User wants to be able to see a website/application which has map on home page, and it's zoom to Claremont city by default and have ability to search required location. 

    - Est completion time 1 week, priority #1

2. User wants the website/application to web responsive. It must be rendered properly on desktop and mobile devices properly.

    - Est completion time 2 weeks, priority #1

3. User wants to be able to navigate/move around the map (zoom in and out) and see different types of maps and change settings of website/application to see it in different themes. User shall not be able zoom out beyond USA country.

    - Est completion time 2 weeks, priority #1

4. User wants to able to select specific category and related multiple subcategories. User wants to able to specify the radius within which specific categories can be located. Application must use YELP search API in backend to query the information related to categories of interest.

    - Est completion time 3 weeks, priority #1

5. User want to able to browse through all search results on map and shall be able to retrieve more information by clicking on specific search result on map.

    - Est completion time 1 week, priority #2

6. User wants to additional information like rating, distance etc. for all search results from specified search location.

    - Est completion time 1 week, priority #2

7. Admin user wants to be able to login into website to view admin dashboard.

    - Est completion time 2 weeks, priority #3

8. Admin user wants to know which filters are selected most often to better understand how users are interacting with the app.

    - Est completion time 2 weeks, priority #3

### Project Dashboard

-  https://github.com/users/katieenns/projects/1 

## PART B

### User Stories broken into Tasks with Team Member Allocated and targeted milestones with iterations

1. User wants to be able to see a website/application which has map on home page, and it's zoom to Claremont city by default and have ability to search required location. 
   * Create a Skelton web application with default basemap. (Pankaj) (MILESTONE #1 - ITERATION #1)
   * Add search widget in web application so that user can search area if interest.  (Pankaj) (MILESTONE #1 - ITERATION #2)

2. User wants the website/application to web responsive. It must be rendered properly on desktop and mobile devices properly.
   * Explore the various HTML frameworks for web responsive design and implemented it in website/application. (Pankaj) (MILESTONE #1 - ITERATION #2)

3. User wants to be able to navigate/move around the map (zoom in and out) and see different types of maps and change settings of website/application to see it in different themes. User shall not be able zoom out beyond USA country.
   * Explore the various types of basemap options available and create widget for user to pick appropriate basemap. (Javier) (MILESTONE #1 - ITERATION #1)
   * Give an option for user to change website/application settings. (Javier) (MILESTONE #1 - ITERATION #2)
   * Restrict user from zooming out beyond US country on map. Need to implement appropriate map scale levels. (Javier) (MILESTONE #2)

4. User wants to able to select specific category and related multiple subcategories. User wants to able to specify the radius within which specific categories can be located. Application must use YELP search API in backend to query the information related to categories of interest.
   * Explore the YELP search API and figure out best way to integrate it in web application. (Katie) (MILESTONE #1 - ITERATION #1)
   * Design the widget in web application with appropriate options for user to select categories. (Katie) (MILESTONE #1 - ITERATION #2)
   * Integrate the YELP’s search API with above widget to query results based on user selection. (Katie) (MILESTONE #1 - ITERATION #2) 
  
5. User want to able to browse through all search results on map and shall be able to retrieve more information by clicking on specific search result on map.
   * Display all search results on map and zoom the map to search results. (Katie) (MILESTONE #1 - ITERATION #2) 
   * Add an ability for use to identify the specific search result information in different pop-up window. (Pankaj) (MILESTONE #2)
   
6. User wants to additional information like rating, distance etc. for all search results from specified search location.
   * Enhance the display of search result to include other appropriate information like distance, reviews etc. (Katie) (MILESTONE #2)
   * Translate similar information into info pop-up windows. (Pankaj) (MILESTONE #2)
  
7. Admin user wants to be able to login into website to view admin dashboard.
   * Explore the flask framework to create admin interfaces. (Hunter) (MILESTONE #1 - ITERATION #2)
   * Create a database model and design the SQLite database to store website/application transactions/hits information. (Hunter) (MILESTONE #1 - ITERATION #2)
   * Create the interfaces for login and sign-up and integrate this with SQLite database. (Hunter) (MILESTONE #2) 

8. Admin user wants to know which filters are selected most often to better understand how users are interacting with the app. 
   * Create the interfaces for admin to retrieve information like which is most search category, which are the most searched subcategories. Display results in tabular format. (Hunter) (MILESTONE #2)


### Features in Milestone 1.0:
* Responsive Web application with ability for users to search required location, pick basemap of their choice and change the application settings.
* Fully integrated YELP's Search API to query and display the search results on map.
* Designed backend database to store information related to usage of website/application.


### 2 Iterations for Milestone 1 (4 weeks)
- Iteration 1 (2 weeks):
  - Create a Skelton web application with default basemap.
  - Explore the various types of basemap options available and create widget for user to pick appropriate basemap.
  - Explore the YELP search API and figure out best way to integrate it in web application.

- Iteration 2 (6 weeks):
  - Add search widget in web application so that user can search area if interest.
  - Explore the various HTML frameworks for web responsive design and implemented it in website/application.
  - Give an option for user to change website/application settings.
  - Design the widget in web application with appropriate options for user to select categories.
  - Integrate the YELP’s search API with above widget to query results based on user selection.
  - Display all search results on map and zoom the map to search results.
  - Explore the flask framework to create admin interfaces.
  - Create a database model and design the SQLite database to store website/application transactions/hits information.

### Velocity

- Timeline: 6 weeks to milestone 1, 5 weeks to milestone 2
- Starting velocity: 95%
   - Total: 8 hours per week
   - Current: 7.6 hours per week

### Burn Down Chart
https://github.com/katieenns/Dream-Team/blob/main/Burn%20Chart.png

### Evidences for periodic stand up meetings:
https://github.com/katieenns/Dream-Team/blob/main/weekly_meetings.docx

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
 
7. Database is available under "website" folder with name "database.db". If database is not available or accidentaly deleted, then you can find backup database available under "website/databasebackup" folder.

## Steps to test the application

1. Install pytest, pytest-flask, and pytest-coverage if they are not already installed from requirements.txt

2. To run tests, navigate into the correct directory (Dream-Team) and run the command 
            
    `pytest`

in the terminal. This will return PASS/FAIL results of the pytests in the "tests" folder.


## Steps to report coverage

1. To determine test coverage, navigate into the correct directory (Dream-Team) and run the command

    `pytest --cov=website` 
        
in the terminal. This will return a chart detailing each file in the project and the amount of coverage the tests provide for them, as well as the total percentage of coverage for the entire project in the website folder. 

    Here is the current coverage report
    
```
    ========================== test session starts ==========================
platform win32 -- Python 3.10.8, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\MS\SoftwareDevelopment\FinalProject\YELP
plugins: my-plugin-0.1.0, cov-4.0.0, emoji-0.2.0, flask-1.2.0
collected 31 items

tests\functional\test_routes.py .................                            [ 54%] 
tests\unit\test_db.py ..                                                     [ 61%] 
tests\unit\test_models.py ............                                       [100%]

---------- coverage: platform win32, python 3.10.8-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
website\__init__.py                  32      3    91%
website\models\__init__.py            0      0   100%
website\models\categories.py          9      1    89%
website\models\dbinteraction.py      80     11    86%
website\models\dbmodels.py           29      0   100%
website\models\yelp.py               20      0   100%
website\viewmodels\__init__.py        0      0   100%
website\viewmodels\admin.py         115     21    82%
website\viewmodels\yelps.py          39      0   100%
-----------------------------------------------------
TOTAL                               324     36    89%

========================= 31 passed, 2 warnings in 4.29s ==========================

```

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

7. Admin user wants to be able to login into admin dashboard. In this dashbaord admin user can configure the categories and subcategoties information displayed in "YELPSearch" widget.

    - Est completion time 2 weeks, priority #3

8. Admin user shall be able to search most freqntly entered categoris and subcategories by user to better understand how users are interacting with the app.p.

    - Est completion time 2 weeks, priority #3

### Project Dashboard

-  https://github.com/users/katieenns/projects/1 

## PART B

### User Stories broken into Tasks with Team Member Allocated and targeted milestones with iterations

1. User wants to be able to see a website/application which has map on home page, and it's zoom to Claremont city by default and have ability to search required location. 
   * Create a Skelton web application with default basemap. (Pankaj) (MILESTONE #1 - ITERATION #1)
   * Add search option in web application so that user can search area if interest.  (Pankaj) (MILESTONE #1 - ITERATION #2)

2. User wants the website/application to web responsive. It must be rendered properly on desktop and mobile devices properly.
   * Explore the various HTML frameworks for web responsive design and implemented it in website/application. (Pankaj) (MILESTONE #1 - ITERATION #2)

3. User wants to be able to navigate/move around the map (zoom in and out) and see different types of maps and change settings of website/application to see it in different themes. User shall not be able zoom out beyond USA country.
   * Explore the various types of basemap options available and create widget for user to pick appropriate basemap. (Javier) (MILESTONE #1 - ITERATION #1)
   * Give an option for user to change website/application settings. (Javier) (MILESTONE #1 - ITERATION #2)
   * Restrict user from zooming out beyond US country on map. Need to implement appropriate map scale levels. (Javier) (MILESTONE #2)

4. User wants to able to select specific category and related multiple subcategories. User wants to able to specify suggested radius within which specific categories can be located. Application must use YELP search API in backend to query the information related to categories of interest.
   * Explore the YELP search API and figure out best way to integrate it in web application. (Katie) (MILESTONE #1 - ITERATION #1)
   * Design the widget in web application with appropriate options for user to select categories. (Katie) (MILESTONE #1 - ITERATION #2)
   * Integrate the YELP’s search API with above widget to query results based on user selection. (Katie) (MILESTONE #1 - ITERATION #2) 
  
5. User want to able to browse through all search results on map and shall be able to retrieve more information by clicking on specific search result on map.
   * Display all search results on map and zoom the map to search results. (Katie) (MILESTONE #1 - ITERATION #2) 
   * Add an ability for use to identify the specific search result information in different pop-up window. (Pankaj) (MILESTONE #2)
   
6. User wants to additional information like rating, distance etc. for all search results from specified search location.
   * Enhance the display of search result to include other appropriate information like distance, rating etc. (Katie) (MILESTONE #2)
   * Translate similar information into info pop-up windows. (Pankaj) (MILESTONE #2)
  
7. Admin user wants to be able to login into admin dashboard. In this dashbaord admin user can configure the categories and subcategoties information displayed in "YELPSearch" widget.
   * Explore the flask framework to create admin interfaces. (Pankaj, Katie, Hunter, Javier) (MILESTONE #1 - ITERATION #2)
   * Create a database model and design the SQLite database to store YELP categories and website/application transactions/hits information. (Pankaj, Katie, Hunter, Javier) (MILESTONE #1 - ITERATION #2)
   * Create the interfaces for login and sign-up and integrate this with SQLite database. (Pankaj, Katie, Hunter, Javier) (MILESTONE #2) 

8. Admin user shall be able to search most freqntly entered categoris and subcategories by user to better understand how users are interacting with the app. 
   * Create the interfaces for admin to retrieve information like which is most search category, which are the most searched subcategories. Display results in tabular format. (Pankaj, Katie, Hunter, Javier) (MILESTONE #2)


### Features in Milestone 1.0:
* Responsive Web application with ability for users to search required location, pick basemap of their choice and change the application settings.
* Fully integrated YELP's Search API to query and display the search results on map.
* Designed backend database to store information related to usage of website/application.


### 2 Iterations for Milestone 1 (6 weeks)
- Iteration 1 (2 weeks):
  - Create a Skelton web application with default basemap.
  - Explore the various types of basemap options available and create widget for user to pick appropriate basemap.
  - Explore the YELP search API and figure out best way to integrate it in web application.

- Iteration 2 (4 weeks):
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

## PART C

### Milestone 1.0 Presentation
https://github.com/katieenns/Dream-Team/blob/main/DreamTeam_Milestone1_Presentation.pptx

### Milestone 1.0 Working Code
Refer to ["How to run the application"](https://github.com/katieenns/Dream-Team/blob/main/README.md#steps-to-run-the-application) section of this readme to run the application. Working code is udated as of today in this repository,

### Testing Strategies

| Storypoint | Description | Testing Strategy |
| ------------- | ------------- | ------------- |
| 1 |  User wants to be able to see a website/application which has map on home page, and it's zoom to Claremont city by default and have ability to search required location | Unit testing for basemap service, Unit testing for Geocoding Service and Manual testing for UI (Need to figure out a way to do automated testing) |
| 2 | User wants the website/application to web responsive. It must be rendered properly on desktop and mobile devices properly | Manual testing for UI (Need to figure out a way to do automated testing)  |
| 3 | User wants to be able to navigate/move around the map (zoom in and out) and see different types of maps and change settings of website/application to see it in different themes | Manual testing for UI (Need to figure out a way to do automated testing) |
| 4 | User wants to able to select specific category and related multiple subcategories. User wants to able to specify suggested radius within which specific categories can be located. Application must use YELP search API in backend to query the information related to categories of interest | Unit testing for YELP API, Unit testing for retrieveing YELP category information, Manual testing for UI (Need to figure out a way to do automated testing) |
| 5 | User want to able to browse through all search results on map and shall be able to retrieve more information by clicking on specific search result on map | Unit testing to test identify feature. Manual testing for UI (Need to figure out a way to do automated testing) |
| 6 | User wants to additional information like rating, distance etc. for all search results from specified search location | Unit testing to check for additional information, Manual testing for UI (Need to figure out a way to do automated testing) |

### Milestone 2.0 

Below are the pending taks for Milestone 2.0

1. Admin user wants to be able to login into admin dashboard. In this dashbaord admin user can configure the categories and subcategoties information displayed in "YELPSearch" widget.
   * Explore the flask framework to create admin interfaces.
   * Create a database model and design the SQLite database to store YELP categories and website/application transactions/hits information.
   * Create the interfaces for login and sign-up and integrate this with SQLite database.

2. Admin user shall be able to search most freqntly entered categories and subcategories by user to better understand how users are interacting with the app. 
   * Create the interfaces for admin to retrieve information like which is most search category, which are the most searched subcategories. Display results in tabular format.

### Burn Down Chart
https://github.com/katieenns/Dream-Team/blob/main/Burn%20Chart%2020221101.png


## PART D 

### Milestone 2.0 Presentation

### Milestone 2.0 Working Code
Refer to ["How to run the application"](https://github.com/katieenns/Dream-Team/blob/main/README.md#steps-to-run-the-application) section of this readme to run and test the application. Working code is udated as of today in this repository.

### Milestone 2.0 Updates
In this Milestone 2.0 release of the project, we have added an admin database for the admin user to configure the categories and subcategories (User Story 7) and to view the most commonly searched subcategories (User Story 8).
We have also updated testing and included functional tests in addition to simple unit tests used in Milestone 1.0

### Project Main Takeaways

Our main takeaways from this project are: 
    
    1. How to integrate GIS mapping / APIs with Python and Flask plugins to create a web-based GIS Application.

    2. Different testing frameworks, including unit testing and pytest. Test driven development is extremely beneficial as it hard to write tests for code after it is written.

    3. Modularizing the codebase to follow best coding practices architecture.


### Burn Down Chart
https://github.com/katieenns/Dream-Team/blob/main/Final_BurnChart_DreamTeam_Milestone2.png

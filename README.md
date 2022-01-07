**Still In Development** 

# Covid-19 Related-Website 

 

## What is this ? 

the files mentioned above represent a website that is being made and developed in order to help with the corona-19 pandemic in many aspects through offering different services 

that other websites/application does not give in the proper way . 

 

## What Was Used ? 

### Developing Environment : PyCharm 

### Languages Used : HTML / CSS / Python 

### Infrastructure : Python Web Framework -> Django 

### Libraries Used : Django Filters , Django URLS , Django Contrib , Django Shortcuts , Django UTILS , Django Templates , Django Cores , 

 

## How Is This Any Different From Other Websites/Applications : 

This website is developed in order to target the audience with the least privilages given , in our case we have decided to focus on the elderly through giving them special 

permissions that other regular users do not have , and it will be designed in order to be able to co-operate under specific covid-19 updates , for example whenever the numbers 

people affected with covid-19 virus has grown bigger , the time gaps between each appointment will be increased according to the vaccination station in the city and according to 

the color of the city , another feature that was added in order to help the elderly get vaccinated and increase the number of the old audience that have been vaccinated is the 

ability to get vaccinated at home because they might face certain difficulities whilst trying to set an appointment / go to an appointment , alongside those priviliges we have 

added and will be adding many features like the ability to report multiple incidents that are related to covid-19 , the ability to read articles while in the process of browsing 

the website , and many other intresting features alongside . 

For the Registeration system we are intending to use a two factor authentication system that will improve the security upon login , for the forms of the login/logout/register systems crispy forms were used in django in order to improve the overall looks and the functionality of the login/logout/register functions . 

 

Sweetify is being used for the temporary messages system , https://github.com/Atrox/sweetify-django . 

 

## How To Use : 

There are 3 ways in order to use the website on your local machine . 

### 1) Cloning The Repository : 

First you will need to navigate to : https://github.com/FadiBadarni/mysite then above the list of files there appears a code button then choose your preffered way of cloning the repository . 

### 2) Downloading The Code : 

First you will need to navigate to : https://github.com/FadiBadarni/mysite then above the list of files there appears a code button then choose download ZIP 

### 3) GitHub Desktop : 

First you will need to navigate to : https://github.com/FadiBadarni/mysite then above the list of files there appears a code button then choose Open with GitHub Desktop 

 

Once the project is on your local machine you will need to open it with pycharm , afterwards a brief installation of CrispyForms is required using pyCharm terminal through hitting the terminal button that is found at the bottom of the pycharm application then inserting these lines of codes inside of it : 

### pip install django-crispy-forms 

### pip install asgiref 

### pip install Django 

### pip install Pillow 

### pip install sqlparse 

Afterwards you can run the server on your local host using : 

### python manage.py runserver 

 

### Info About The DataBase : 

Currently we are using the built in database that django provides , for future references we will be using either firepase or sqlite3 

 

## Navigation In The Website : 

The website is made so it can be easy to understand and navigate in , first the user would be required to register a new account , afterwards the user goes through the login process with being able to reset his password at any given time the user would like to (through email verfication) , after logging in a new tab in the navigation bar appears in addition to the other tabs which is appointment booking because that functionality is only available upon logging into an acount . 

The navigation bar contains many elements which are the following : 

#### 1) Home button : 

Takes the user to the home page . 

#### 2) Book An Appointment button : 

Takes the user to setting appointment page (only appears if user is logged in) , the appointment page contains a time table which covers an entire day's of work hours alongside having the entire days of the week available for setting an appointment in a time that is not taken . 

#### 3) FAQ : 

The FAQ section is a section that is made for questions and answers about the corona virus and some informative videos alongside. 

#### 4) About : 

The about page contatins various information on the website and the staff alongside information about the virus itself and helpful videos 

#### 5) Contact : 

The contact page contains a contact form that when filled correctly will be sent to be reviewed by the web's crew 

#### 6) Profile : 

The profile page is where a user can see his personal info (email & name) and edit his details when needed . 

 

## The HomePage : 

The home page contains many elements which will be listed below : 

### 1) COVID-19 Vaccination Variety + Short Info (SECTION) : 

contains various information about various corona vaccinations . 

### 2) Corona-Related Links : 

contains a list of links that lead into different websites that handle various informations about the corona virus . 

### 2) The countries with the highest patient growth : 

A Simple table that stats the leading countries in the highest patient growth 

 

## FAQ Page : 

The FAQ page contains various information in different aspects : 

### 1) Questions & Answers : 

Contains questions and answers in different topics 

 

## About Page : 

The about page Contains different information on the website's staff and the corona virus 

 

## Contact Page : 

The contact page contains a simple contact form to be sent to the website's crew for review 

 

## Appointments Page : 

This page contains the main idea of the website , in which the user is able to book an appointment in the time he wants in the day he desires , when a user books an appointment it will be saved and available for view in the user's profile where a button appears that makes the user allowed to view his appointments and the status of each appointment. 

 

## General Info : 

The project is being developed by a second year software engineering students as a project of "Software Engineering Basics" . 

For Further Questions : fadybd1@gmail.com 

# DRF_Friends API

DRF_Friends API is the backend service used by the [Friends Wildlife](https://github.com/email2ify/friends).
<hr>
<br>

## Table of Contents

* [Agile Planning](#Agile-Planning)
    * [User Stories](#User-Stories)
    * [Epics](#Epics)
* [API End Points](#API-End-Points)
* [Future Features](#Features-Left-to-Implement)
* [Database Design](#Database-Design)
* [Security](#Security)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment) 
    * [Heroku Deployment](#Heroku-Deployment)
    * [GCP](#Google-Cloud-Platform)
    * [Fork Project](#Fork-Project)
* [Credits](#Credits)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

## Development Goals

The purpose of this API is to provide a backend service to allow the Friends users front end applications to render, Create, Read, Update and Delete operations via the user interface.
<hr>
<br>

## Agile Planning

This project was developed using agile methodologies and features in incremental loop. 

Stories were assigned to epics, prioritized under the Todo, In progress, and Done. It was done this way to ensure that all requirements were completed first to give the project a balance, with features being added one after the other..

The Kanban board was created using github projects and can be located [here](https://github.com/users/email2ify/projects/13/views/1) and can be viewed to see more information on the project cards.The documentation tasks have an acceptance criteria in order to define the functionality that marks that story as done or in progress.

![Kanban](https://.PNG)

### Epics

**Set Up**

This aspect covers all the initial setup of the Django application and Django REST Framework and coding features.

**Posts**

This aspect covers all API endpoint creation and database connections relating to the CRUD functionality of user posts.

**Comments**

This aspect covers all API endpoint creation and database connections relating to the CRUD functionality of user comments in relation to posts.

**Profiles**

This aspect covers all API endpoint creation and database connections relating to the CRUD functionality of user created profiles.

**User**

This aspect covers all API endpoint creation and database connections relating to the CRUD functionality of users who register.


<hr>
<br>

### User Stories

**By Epics** 

**Setup**

* Create the google cloud and create the connection to the project so that static images can be uploaded by users.

* Create a new account so that I can access all the features for signed up users


**Posts**

* For user, to be able to view edit or delete a post
* For user, to able to create a post and list posts

**Profiles**

* I needed to create a new blank profile with default image when a user is created.
* I needed to create list of profiles diplaying on a list

### API Endpoints

User Story:

* User can create a base project set up so that I can build out the features.`

Implementation:
The settings were also edited to hide any secret variables and set dev and production environments.

User Story:

* Create the google cloud and create the connection to the project so that static images can be uploaded by users.

Implementation:

A google cloud bucket was created and a service account created to allow image uploads via the service account.


User Story:

As a user I can create a new account so that I can access all the features for signed up users

Implementation:

Django rest framework and dj_rest_auth were installed and added to the url patterns and site packages to make use of their built in authentication system.

User Story:

Create api views, so that they are available to the front end

Implementation:

Methods:
* POST - Used to create a users
* GET - Used to retrieve a list of users

Endpoint: /users/<int:pk>/

Methods:
* GET - Used to view single user profile
* PUT - Used to update an user profile
* DELETE - Used to delete user profile


User Story:

As a user, I want to be able to view edit or delete a post

As a user, I want to able to create a post and list posts

Implementation:

Endpoint: /posts/

Methods:
* POST - Used to create post
* GET - Used to get a list of posts

Endpoint: /posts/<int:pk>/

Methods:
* GET - Get a single post
* PUT - Used to update a single post
* DELETE - Used to delete a post


User Story:

I want to create a new blank profile with default image when a user is created.

Implementation:

In the profiles app, a signal was created in order to create a new user profile on signup.


User Story:

 I want user to be able to get a list of profiles

Implementation:

Endpoint: /profiles/

Methods:
* POST - Used to create post
* GET - Used to get a list of posts

Endpoint: /profiles/<int:pk>/

Methods:
* GET - Get a single profile
* PUT - Used to update a single profile
* DELETE - Used to delete a profile


## Security

A permissions class was added called "IsOwnerOrReadOnly" to ensure only users who create the content are able to edit or delete it and the GCP IAMS permissions for service account.
to minimum permissions granted.

## Technologies

* Git
    * Used for version control
* Github
    * Repository for storing code base and docs
* Django
    * Main framework used for application creation
* Django REST Framework
    * Framework used for creating API
* Google Cloud Platform
    * Used for static image hosting
* Heroku
    * Used for hosting the application


<hr>
<br>

## Python Packages
<details open>
<summary> Details of packages </summary>

* dj-database-url==1.0.0
    * Used to parse the DATABASE_URL connection settings
* dj-rest-auth==2.2.5
    * Used with auth system
* Django==4.1.1
    * Main framework used to start the project
* django-allauth==0.50.0
    * Used for authentication
* django-cors-headers==3.13.0
    * Used for Cross-Origin Resource Sharing (CORS) headers to responses
* django-filter==22.1
    * Used to filter API results in serializers
* django-storages==1.13.1
    * Used to help connect with the google cloud storage bucket
* djangorestframework==3.13.1
    * Framework used to build the API endpoints
* djangorestframework-simplejwt==5.2.0
    * Used with djange rest framework to create access tokens for authentication
* gunicorn==20.1.0
    * Used for deployment of WSGI applications
* Pillow==9.2.0
    * Imaging Libray - used for image uploading
* psycopg2==2.9.3
    * PostgreSQL database adapter to allow deployed application to perform crud on the postgresql db
* PyJWT==2.5.0
    * For creating the Python Json Web Tokens for authentication

Installed as package dependcies with above installations:
* asgiref==3.5.2
* autopep8==1.7.0
* cachetools==5.2.0
* certifi==2022.6.15.1
* cffi==1.15.1
* charset-normalizer==2.1.1
* cryptography==38.0.1
* defusedxml==0.7.1
* idna==3.3
* oauthlib==3.2.1
* protobuf==4.21.5
* pyasn1==0.4.8
* pyasn1-modules==0.2.8
* pycodestyle==2.9.1
* pycparser==2.21
* python3-openid==3.2.0
* pytz==2022.2.1
* requests==2.28.1
* requests-oauthlib==1.3.1
* rsa==4.9
* six==1.16.0
* sqlparse==0.4.2
* toml==0.10.2
* types-cryptography==3.3.23
* tzdata==2022.2
* urllib3==1.26.12

Auto installed as package dependencies with django-storages[GOOGLE] to aid connection to google cloud buckets for static image hosting:
* google-api-core==2.10.0
* google-auth==2.11.0
* google-cloud-core==2.3.2
* google-cloud-storage==2.5.0
* google-crc32c==1.5.0
* google-resumable-media==2.3.3
* googleapis-common-protos==1.56.4
</details>
<hr>
<br>

## Testing

Unit tests in posts app

![Post Tests]()


**Validator Results**

All folders were run through flake8. Several issues appeared with various reasons, lines too long, blank spaces, indentation and docstrings.

I was ......


**Bugs and their fixes**

 500 error as a bug occurred on post and profile form submissions, which I later removed the dublicate causing the errors
<hr>
<br>

## Deployment

## Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository.

```git push``` - This command was used to push all committed code to the remote repository on github.

<hr>
<br>

## Heroku Deployment

The site was deployed to Heroku with the foolwing steps:

* Navigate to heroku and create an account
* Click the new button in the top right corner
* Select create new app
* Enter app name
* Select region and click create app
* Click the resources tab and search for Heroku Postgres
* Select hobby dev and continue
* Go to the settings tab and then click reveal config vars
* Add the following config vars:
  * SECRET_KEY: (Your secret key)
  * DATABASE_URL: (This should already exist)
  * ALLOWED_HOST:
  * CLIENT_ORIGIN: url for the client front end react application that wil be making requests to these APIs
  * CLIENT_ORIGIN_DEV: address of the local server used to preview and test UI during development of the front end client application
  * GOOGLE_APPLICATION_CREDENTIALS:
  * GOOGLE_CREDENTIALS: json file with authentication keys and tokens to access the google cloud bucket where images are stored
  * GS_BUCKET_NAME: Upload images to.

* Click the deploy tab
* Scroll down to Connect to GitHub and sign in , authorize when prompted
* In the search box, find the repositoy you want to deploy and click connect
* Scroll down to Manual deploy and choose the main branch
* Click deploy

<hr>
<br>

## Google Cloud Storage

To set up cloud and service account. Please see - [Medium Article](https://medium.com/@mohammedabuiriban/how-to-use-google-cloud-storage-with-django-application-ff698f5a740f). The service account credentials will be needed for deployment.

**Code** 

Packages needed for deployment:

* django-storages[google]
* Pillow

Create a profile file with the following line inside:

```echo ${GOOGLE_CREDENTIALS} > /app/ga-creds.json```

This line is used to instruct heroku that the GOOGLE_CREDENTIALS var is called ga-creds.json

**Heroku**

1. Log in to heroku and open the apps name
2. Click settings
3. Click Config vars
4. Add the following variables:

    * Key: GOOGLE_APPLICATION_CREDENTIALS -  Value: ga-creds.json
    * Key: GOOGLE_CREDENTIALS - Value: json contents of the service account key
    * Key: GS_BUCKET_NAME - Value: Name of the cloud where files are stored


Windows:

```
python -m venv venv \
venv/Scripts/activate \
pip install -r requirements.txt
```

Mac:

```
python -m venv venv \
source venv/bin/activate \
pip install -r requirements.txt
```

### Forking

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.


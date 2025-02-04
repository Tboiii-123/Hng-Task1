# Hng-Task-0
#Hng internship

#Project Description

A simple public Api developed as a python Back-edn developer, which retuens JSON response>

The data contains

>The registered email address(used to register on HNG 12 Slack workspace)

>THe current datetime in ISO 8601 format (UTC)

>The Github URL of the project's codebase


The Api what build with python using the django rest_framework.

And it was also deployed on render for public access


API Endpoint

URL :https://hng-task-0-hhmx.onrender.com/api/

Response:

```
{
  "email": "lawalhussein775@gmail.com",
  "current_datetime": "2025-01-30T20:08:06.847424",
  "github_url": "https://github.com/Tboiii-123/Hng-Task-0"
}
```


Example Usage:

You can test the Api on Postman, by adding the endpoint url in it and using a GET request method 

Set up Instruction:

1.Clone the repository

git clone https://github.com/Tboiii-123/Hng-Task-0.git

2.Install Packages on cmd

>pip install django

>pip install django_restframework

3.To start Server:

>Go to your  where manage.py is located in the folder  on cmd

>The run this command

>python manage.py runserver

4.Access the endpoint on the local machine with the /api/ appended to it

Deployment:

It was deployed on render platform



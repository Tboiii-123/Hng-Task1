# Hng-Task-0
#Hng internship

#Project Description

A simple public Api developed as a python Back-end developer, which returns JSON response

The data contains

>Actual Number needed

>The prime number of the actual number

>The perfect number of the actual number

>The properties of the actual number either Armstrong, odd , even or Armstrong and  odd/even 

>The sum of all the digits

>Fun fact about the actual number fecteched from an api called numperapi using the math type

The Api what build with python using the django rest_framework.

And it was also deployed on render for public access


API Endpoint

URL :https://hng-task1-n172.onrender.com/api/?num=371

Response:

```
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "Armstrong",
    "Odd"
  ],
  "digit_sum": 11,
  "fun_fact": "371 is a narcissistic number."
}
```


Example Usage:

You can test the Api on Postman, by adding the endpoint url in it and using a GET request method 

Set up Instruction:

1.Clone the repository
```
git clone https://github.com/Tboiii-123/Hng-Task1.git
```

2.Install Packages on cmd
```

>pip install django

>pip install django_restframework
```

3.To start Server:

>Go to your  where manage.py is located in the folder  on cmd

>The run this command

>python manage.py runserver

4.Access the endpoint on the local machine with the /api/ appended to it

Deployment:

It was deployed on render platform



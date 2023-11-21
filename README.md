![Django CI](https://github.com/claraj/python-unittest-actions/actions/workflows/django.yml/badge.svg)

# Example project with Django unit tests and GitHub actions

This web app should have two pages, 

* The welcoming home page http://127.0.0.1:8000/
* The extremely accurate math page http://127.0.0.1:8000/two_plus_two 

But it looks like the home page message is wrong, and the math is not correct either. 

Fortunately, there are some tests that can help identify problems, or verify things are working. 

Can you fix the code?

## Running the app

Fork this repository and clone it to your computer.

Install dependencies `pip install -r requirements.txt`    (optionally create a virtual environment first)  
Run the app with `python manage.py runserver`

## Running the tests locally

`python manage.py test`

## GitHub Actions

These are tasks that are performed when an event happens at GitHub. The Actions for this repository are defined in the .github/worklows/django.yml file. You don't need to understand every detail, but have a look at this file, what do you notice? 

## Your tasks

The tests are correct. They are failing because there are bugs in the code.  

1. Create a new branch
2. Fix one of the problems, test by running the app and by running the tests on your computer
3. Push your branch to GitHub and create a pull request
4. Observe output from Actions in the pull request
5. In the same branch, fix the other problem, test by running the app and by running the tests on your computer
6. Push your branch to GitHub
7. Observe output from Actions in the pull request



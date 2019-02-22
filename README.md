# Description

Budget api is a simple budget application that was written as an api using django/python with DRF to manage projects budget and show how much expenses was used and how much is still left.

# Installation

- simply clone the project and copy it into a virtual environment
- open terminal and navigate to the environment folder then activate it, after that navigate to the api project folder
- install the packages from requirments.txt by running `pip -r install requirements.txt`
- run `python manage.py runserver`
- you are ready to go now

# Currently there are 3 endpoints

## 1- projects ("/api/projects/")

- CRUD system for projects.

## 2- Categories ("/api/categories/")
- CRUD system for categories.

## 3- Expenses ("/api/expenses/")
- Crud system for expenses, note that expenses has a relationship with projects and expenses.

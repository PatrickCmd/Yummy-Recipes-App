[![Build Status](https://travis-ci.org/PatrickCmd/Yummy-Recipes-App.svg?branch=master)](https://travis-ci.org/PatrickCmd/Yummy-Recipes-App)
[![Coverage Status](https://coveralls.io/repos/github/PatrickCmd/Yummy-Recipes-App/badge.svg?branch=master)](https://coveralls.io/github/PatrickCmd/Yummy-Recipes-App?branch=master)
# Yummy-Recipes-App
Yummy recipes app is an application that allows users  to create, save and share meeting the needs of keeping track of awesome food recipes.

## Functionality
- `Signup` Enables user to create an account
- `Signin` Enables user to login and access his/her dashboard
- `View Account Details` Enables to view his/her account details
- `Add Recipe category` Enables user to create his/her recipe categories

## Requirements
`python 3.4+, python-pip, virtualenv, flask`

## Installation
First clone this repository
```
$ git clone https://github.com/PatrickCmd/Yummy-Recipes-App.git
$ cd Yummy-Recipes-App.git
```
Create virtual environment and install it
```
$ virtualenv env
$ source/env/bin/activate
```
Then install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python run.py
```
To run tests run this command at the console/terminal
```
nosetests
```

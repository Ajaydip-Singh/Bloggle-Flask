# Welcome to Bloggle

Bloggle is a Flask app that is deployed on heroku [here](https://bloggleapp.herokuapp.com/login). Users can register, login, and create blogs to share with the rest of the user base. Users have an account page where they can set an image for their profile picture and as well as change usernames and passwords. Bloggle is responsive so it works great on different screen sizes. Go ahead and give it a try if you are interested! Here is a short preview. 

<img src='http://g.recordit.co/fJ1BMSH1FK.gif' title='Video Walkthrough' alt='Video Walkthrough' />


# How to contribute


1. Clone the forked repo to a "local" directory (on your computer).

```
git clone https://github.com/Ajaydip-Singh/Bloggle-Flask.git
```

then change into the directory.

```
cd Bloggle-Flask
```

3. Create a branch for the new feature being contributed.

```
git checkout -b [name-of-branch]
```

4. After the feature has been implemented git push your branch and create a pull request. 




## Run Virtual Environment

Virtual environment is a key component in ensuring that the application is configured in the right environment

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

On Windows:

```
python -m pip install virtualenv
```

##### Usage
Creation of virtualenv:

    $ virtualenv -p python3 venv

If the above code does not work, you could also do

    $ python3 -m venv venv

To activate the virtualenv:

    $ source venv/bin/activate

Install dependencies in virtual environment:

    $ pip3 install -r requirements.txt

Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

To deactivate the virtualenv (after you finished working):

    $ deactivate

## Environment Variables

All environment variables are stored within the `.env` file and loaded with dotenv package.

**Never** commit your local settings to the Github repository!

## Run Application

Start the server by running:

    $ export FLASK_ENV=development
    $ python3 run.py




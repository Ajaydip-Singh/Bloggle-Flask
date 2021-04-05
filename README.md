# Welcome to BLOGit

## Setup

1. Make sure you have git installed on your device, run the following command on the terminal:

```
git --version
```

2. Clone the repo to a "local" directory (on your computer), 

```
git clone https://github.com/Ajaydip-Singh/blog_it_web_app.git
```

then change into the directory

```
cd blog_it_web_app
```

3. To make sure everything is up to date on your end, run

```
git pull
```

4. Always create a branch for any new task

```
git checkout -b [name-of-branch]
```

5. If you are using Visual Studio Code to contribute, you can use

```
code .
```

and make your contributions in the branch you have created.

6. Save all changes in Visual Studio Code, then run

```
git add .
git status
git commit -m "A clear message about contribution"
git push
```

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
    $ export FLASK_APP=web
    $ python3 -m flask run


# Preview of BLOGit

<img src='http://g.recordit.co/Iv4wgC7Eiv.gif' title='Video Walkthrough' width='500' alt='Video Walkthrough' />

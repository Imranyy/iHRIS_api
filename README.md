# README #


### Requirements
- [Python3](https://www.python.org/)
- [Pipenv](https://pipenv.kennethreitz.org/en/latest/)

### How do I get set up? ###

* `git clone https://github.com/uonafya/iHRIS_api`
* `cd iHRIS_api` to navigate to the project folder
* `pipenv shell` to create and activate virtual environment
* `pipenv install` to install the dependencies
* `touch .env` to create a file where you will place the environment variable
*  `cp .env.sample .env` to copy content of .env.sample to .env then replace the values with your real data
* `source .env` to export environment variables
* `python manage.py runserver` to start the server
* `celery -A app worker -l info` to start celery worker
* `celery -A app beat -l info` to start celery beat
* Navigate to development server at `http://127.0.0.1:8000/`
# NPC Print Utility
Print utility for Schematics NPC 2020

## Requirements
1. python 3.6+
2. pip
3. python virtualenv
4. PostgreSQL

## Setup
1. Create virtualenv to store python dependencies, activate.
2. Install required dependencies with `pip install -r requirements.txt`
3. Create a user in PostgreSQL, and create a database for NPC Print Utility.
4. **Update secret key and database credentials in Django settings!**
5. Create migrations and migrate project with `python manage.py makemigrations`, `python manage.py migrate`

## Running
1. Make sure virtualenv is activated and PostgreSQL service is running.
2. Run webserver with `daphne npcprintutil.asgi:application`

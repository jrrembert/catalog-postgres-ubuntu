#!/usr/bin/env python
"""
Author: J. Ryan Rembert
Project: catalog
Source: https://github.com/jrrembert/catalog

Copyright (C) 2015 J. Ryan Rembert. All rights reserved.

Redistribution of source code perfectly cool as long as the
above copyright notice is provided and you don't sue me if
something (somehow) explodes. Unless it explodes into a
rainbow of mutant dinosaurs made out of cookie batter.
Then I assume complete credit.
""" 
import json

# Define application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable for development environment
DEBUG = False

# Define the database we are working with
# Note: This path will not play nice with Vagrant synced folders.
#       Make sure path corresponds to environment where you run your code.
SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/app.db'.format(BASE_DIR)
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "change_me"

# Secret key for signing cookies
SECRET_KEY = "secretsecrets"

# Google Sign-In 
CLIENT_SECRET_PATH = '{}/../client_secrets.json'.format(BASE_DIR)
OAUTH_CREDENTIALS = {
    'google': {
        'client_id': json.loads(
            open(CLIENT_SECRET_PATH, 'r').read())['web']['client_id'],
        'client_secret': json.loads(
            open(CLIENT_SECRET_PATH, 'r').read())['web']['client_secret'],
        'revoke_url': 'https://accounts.google.com/o/oauth2/revoke?token='
    }
}

# class Config(object):
#     DEBUG = False
#     TESTING = False
#     DATABASE_URI = 'sqlite:///testdb.db'


# class DevelopmentConfig(Config):
#     SECRET_KEY = "Not so secret key"
#     DEBUG = True


# class ProductionConfig(Config):
#     SECRET_KEY = 'vj2tj2@C#r2c89PP98P3HC32fjio233$r%t9d$23r3fvnti5588!!24'
#     DATABASE_URI = ''


# class TestingConfig(DevelopmentConfig):
#     TESTING = True

try:
    from local_config import *
except ImportError:
    print("Local config file not found. Loading base config.")

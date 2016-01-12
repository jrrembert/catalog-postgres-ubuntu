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
# Define application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Enable for development environment
DEBUG = True

# Define the database we are working with
DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
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
CSRF_SESSION_KEY = "secret_csrf"

# Secret key for signing cookies
SECRET_KEY = "secretsecrets"

# Google Sign-In 
CLIENT_SECRET_PATH = '{}/../client_secrets.json'.format(BASE_DIR)

# Fixture values if using teamdata.py
USER_EMAIL = ''
USER_NAME = ''
USER_PICTURE = ''

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
import random
import string


# Enable for development environment
DEBUG = True

# Define application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

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
CSRF_SESSION_KEY = 'change_me'

# Secret key for signing cookies
SECRET_KEY = ''.join(random.choice(string.ascii_uppercase + 
                                   string.ascii_lowercase + 
                                   string.digits) for x in xrange(32))

# Google Sign-In 
CLIENT_SECRET_PATH = '{}/../client_secrets.json'.format(BASE_DIR)

# Fixture values if using teamdata.py
USER_EMAIL = 'rynliquid@gmail.com'
USER_NAME = 'J. Ryan Rembert'
USER_PICTURE = 'https://pbs.twimg.com/profile_images/588416345416404992/y8EvAjvm.jpg'

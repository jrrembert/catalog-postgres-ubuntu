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
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from catalog_project import db


# # Prepare and connect to database
# engine = create_engine(DATABASE_URI, convert_unicode=True)

# # A scoped_session handles threading automatically
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))

# Base = declarative_base()
# Base.query = db_session.query_property()

def init_db():
    """ Import all modules that might define models so they
        will be property registered on the metadata. Otherwise
        they will have be imported first before calling init_db().
    """
    import catalog_project.models
    db.create_all()

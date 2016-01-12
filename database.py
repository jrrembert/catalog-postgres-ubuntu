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
from catalog_project import db


def init_db():
    """ Import all modules that might define models so they
        will be property registered on the metadata. Otherwise
        they will have be imported first before calling init_db().
    """
    import catalog_project.models
    db.create_all()

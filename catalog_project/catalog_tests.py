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
import os
import unittest
import tempfile

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Sports, Base, Teams, Users

from config import DATABASE_URI

from run import app











class CatalogTestCase(unittest.TestCase):



    def setUp(self):
        # sqlite is a filesystem-based db so just create temp file
        # db_fd is an integer value needed to call os.close() on the file.
        self.db_fd, self.db_name = tempfile.mkstemp()
        self.app = app
        


        app.config['TESTING'] = True
        self.app.config.update(dict(
            TESTING=True,
            DATABASE="sqlite://{0}".format(self.db_name)
            ))


        self.client = self.app.test_client()
        engine = create_engine(app.config['DATABASE'])
        Base.metadata.bind = engine
        db_session = sessionmaker(bind=engine)
        session = db_session()
        print(app.__dict__)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.db_name)



    def test_empty_db(self):
        root = self.client.get('/')
        print(root.data)
        self.assertIn('Football', root.data)


if __name__ == '__main__':
    unittest.main()
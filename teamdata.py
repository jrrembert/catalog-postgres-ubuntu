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
import datetime

from catalog_project import app, db
from catalog_project.models import Sports, Teams, Users


session = db.session()

# Create dummy user
user1 = Users(name=app.config['USER_NAME'], 
              email=app.config['USER_EMAIL'],
              picture=app.config['USER_PICTURE'], 
              created_date=datetime.datetime.now())
session.add(user1)

# Create sports
sports = [Sports(user_id=1, name="Baseball", 
                 created_date=datetime.datetime.now()),
          Sports(user_id=2, name="Football", 
                 created_date=datetime.datetime.now()),
          Sports(user_id=1, name="Basketball", 
                 created_date=datetime.datetime.now())]
session.add_all(sports)

# Commit sports so that sqlite will assign them an id
session.commit()  

# Teams for Baseball
baseball_teams = [Teams(user_id=1, name="Atlanta Braves", wins=10,
                        losses=5, league = 'NL', sport_id=sports[0].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/atlanta-braves-logo.jpeg"),
                  Teams(user_id=1, name="St. Louis Cardinals", wins=10,
                        losses=5, league = 'NL', sport_id=sports[0].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/st-louis-cardinals-logo.jpg"),
                  Teams(user_id=1, name="Los Angeles Dodgers", wins=10,
                        losses=5, league = 'NL', sport_id=sports[0].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/los-angeles-dodgers-logo.jpg"),
                  Teams(user_id=1, name="Texas Rangers", wins=10,
                        losses=5, league = 'AL', sport_id=sports[0].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/texas-rangers-logo.png"),
                  Teams(user_id=1, name="Tampa Bay Rays", wins=10,
                        losses=5, league = 'AL', sport_id=sports[0].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/tampa-bay-devil-rays-logo.jpg")]

session.add_all(baseball_teams)

# Teams for Football
football_teams = [Teams(user_id=1, name="Atlanta Falcons", wins=10, 
                        losses=5, league = 'AFC', sport_id=sports[1].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/atlanta-falcons-logo.jpg"),
                  Teams(user_id=1, name="New England Patriots", wins=10,
                        losses=5, league = 'AFC', sport_id=sports[1].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/new-england-patriots-logo.jpg"),
                  Teams(user_id=1, name="Indianapolis Colts", wins=10,
                        losses=5, league = 'AFC', sport_id=sports[1].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/indianapolis-colts-logo.png"),
                  Teams(user_id=1, name="Denver Broncos", wins=10,
                        losses=5, league = 'NFC', sport_id=sports[1].id, 
                        created_date=datetime.datetime.now(),
                        logo="/static/images/denver-broncos-logo.jpg"),
                  Teams(user_id=1, name="Seattle Seahawks", wins=10,
                        losses=5, league = 'NFC', sport_id=sports[1].id, 
                         created_date=datetime.datetime.now(),
                         logo="/static/images/seattle-seahawks-logo.jpg")]

session.add_all(football_teams)

# Teams for Basketball
basketball_teams = [Teams(user_id=2, name="Atlanta Hawks", wins=10, 
                          losses=5, league = 'Eastern Conference', 
                          sport_id=sports[2].id, 
                          created_date=datetime.datetime.now(),
                          logo="/static/images/atlanta-hawks-logo.png"),
                    Teams(user_id=2, name="Indiana Pacers", wins=10, 
                          losses=5, league = 'Eastern Conference', 
                          sport_id=sports[2].id, 
                          created_date=datetime.datetime.now(),
                          logo="/static/images/indiana-pacers-logo.jpg"),
                    Teams(user_id=2, name="Detroit Pistons", wins=10, 
                          losses=5, league = 'Eastern Conference', 
                          sport_id=sports[2].id, 
                          created_date=datetime.datetime.now(),
                          logo="/static/images/detroit-pistons-logo.png"),
                    Teams(user_id=2, name="Los Angeles Clippers", wins=10, 
                          losses=5, league = 'Western Conference', 
                          sport_id=sports[2].id, 
                          created_date=datetime.datetime.now(),
                          logo="/static/images/los-angeles-clippers-logo.jpg"),
                    Teams(user_id=2, name="Denver Nuggets", wins=10, 
                          losses=5, league = 'Western Conference', 
                          sport_id=sports[2].id, 
                          created_date=datetime.datetime.now(),
                          logo="/static/images/denver-nuggets-logo.png")]

session.add_all(basketball_teams)
session.commit()

num_teams = len(baseball_teams) + len(football_teams) + len(basketball_teams)

print("Added {} sports and {} teams.").format(len(sports), num_teams)

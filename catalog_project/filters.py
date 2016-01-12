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
import time



def convert_datetime(value, format="raw"):
    
    year = datetime.timedelta(days=365)
    week = datetime.timedelta(days=7)
    day = datetime.timedelta(seconds=86400)
    hour = datetime.timedelta(seconds=3600)
    minute = datetime.timedelta(seconds=60)



    if format=="raw":
        return value
    if format=="human-short":
        now = datetime.datetime.now()
        time_delta = now - value
        if time_delta.days < 1:
            if time_delta < minute:
                return("Created {} second(s) ago".format(time_delta.seconds))
            elif time_delta < hour:
                return("Created {} minute(s) ago".format(time_delta.seconds / minute.seconds))
            else:
                return("Created {} hour(s) ago".format(time_delta.seconds / hour.seconds))
        elif time_delta < week:
            return("Created {} day(s) ago.".format(time_delta.days))
        elif time_delta < year: 
            return("Created {} week(s) ago.").format(time_delta.days / week.days)
        else:
            return("Created {} year(s) ago.").format(time_delta.days / year.days)



# # Raw test case
# print(convert_datetime(datetime.datetime(2015, 1, 1)))

# # Seconds ago

# n = datetime.datetime.now()
# print(n)
# time.sleep(2)
# print(convert_datetime(n, format="human-short"))
# # Minutes ago
# print(convert_datetime(datetime.datetime(2015, 8, 12, 0, 50), format="human-short"))
# # Hours ago
# print(convert_datetime(datetime.datetime(2015, 8, 11, 20), format="human-short"))
# # Days ago
# print(convert_datetime(datetime.datetime(2015, 8, 8), format="human-short"))
# # Months ago
# print(convert_datetime(datetime.datetime(2015, 6, 1), format="human-short"))
# # Years ago
# print(convert_datetime(datetime.datetime(2013, 1, 1), format="human-short"))


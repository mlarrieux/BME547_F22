# time_server.py

from ast import AsyncFunctionDef
from importlib.resources import as_file
from turtle import hideturtle
from flask import Flask, jsonify, request
import numpy as np
import requests
import datetime

app = Flask(__name__)


@app.route("/", methods=['GET'])
def server_info():
    return "This is Mimi's time server."


@app.route("/time", methods=['GET'])
def get_current_time():
    now = datetime.datetime.now()
    current_time = now.time().isoformat()
    message = "The current time in military time is {}".format(current_time)
    return message


@app.route("/date", methods=['GET'])
def get_current_date():
    now = datetime.datetime.now()
    current_date = now.date().isoformat()
    message = "The current date is {}".format(current_date)
    return message


@app.route("/age", methods=["POST"])
def get_current_age():
    '''
        incoming_json = {'date': "10/10/1999",
                         'units': "years"}
        in order month, day, year
    '''
    now = datetime.datetime.now()
    try:
        in_data = request.get_json()
        if in_data['units'] == 'years':
            dt = datetime.datetime.strptime(in_data['date'], "%m/%d/%Y")
            tdelt = now - dt
            age_in_years = (tdelt.days)/365
            return "The age in years is {}".format(age_in_years)
        else:
            return "The units must be years. Please try again."
    except Exception:
        return "Either incoming json was not passed in or the"\
               " contents is invalid. Please pass in json data"\
               " in the format {'date': '10/10/1999', units: 'years'}"\
               " in the order month, day, year."


@app.route("/until_next_meal/<meal>", methods=['GET'])
def get_time_to_meal(meal):
    context_message = "Breakfast occurs at 8:00am, Lunch at 12:30pm,"\
                      " and Dinner at 7:00pm.<br/><br/>"
    now = datetime.datetime.now()
    curr_time = now.time()

    if meal == 'breakfast':
        bfast_time = datetime.time(hour=8)
        if curr_time <= bfast_time:
            diff = datetime.datetime(now.year, now.month, now.day, hour=8)\
                - now
        else:
            next_bfast = datetime.datetime(now.year, now.month, now.day,
                                           hour=8) + datetime.timedelta(days=1)
            diff = next_bfast - now
        return context_message + "Time to breakfast is {} hours".\
            format(diff.seconds/3600)
    elif meal == 'lunch':
        lunch_time = datetime.time(hour=12, minute=30)
        if curr_time <= lunch_time:
            diff = datetime.datetime(now.year, now.month, now.day, hour=12,
                                     minute=30) - now
        else:
            next_lunch = datetime.datetime(now.year, now.month, now.day,
                                           hour=12, minute=30) +\
                                           datetime.timedelta(days=1)
            diff = next_lunch - now
        return context_message + "Time to lunch is {} hours".\
            format(diff.seconds/3600)
    elif meal == 'dinner':
        dinner_time = datetime.time(hour=19)
        if curr_time <= dinner_time:
            diff = datetime.datetime(now.year, now.month, now.day, hour=19)\
                                     - now
        else:
            next_dinner = datetime.datetime(now.year, now.month, now.day,
                                            hour=19) +\
                                            datetime.timedelta(days=1)
            diff = next_dinner - now
        return context_message + "Time to dinner is {} hours".\
            format(diff.seconds/3600)
    else:
        return "This is not a valid meal. Please enter a url in the format "\
            "of url/until_next_meal/<meal> where meal is equal to breakfast, "\
            "lunch, or dinner."


if __name__ == "__main__":
    app.run()

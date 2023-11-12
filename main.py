#!/usr/bin/env python3

### Standard library imports
import os 
import time
import requests
import csv
from datetime import datetime

### Related third-party imports.
from buildhat import Motor, ForceSensor
import schedule

### Local application/library specific imports
from api_call import api_call
from yoy_growth import show_on_dial

### GLOBAL_CONSTANTS
motor = Motor('A')
SALES_GOAL = 6200000
MAX_RANGE_OF_MOTER = 8685
crontab = False
api_result = [0, -30]

### Function and Class Definitions

class MyClass:
    # Class docstring
    def __init__(self):
        pass

def main_function():
    # Function docstring
    pass

### Main Function

def main():

    show_on_dial(20)
    
    # Test for connection
    check_internet_connection()

    # reset motor to 0 degrees
    start_postion = motor.get_position()
    motor.run_for_degrees(start_postion*-1)
    time.sleep(3)

    # Run the first job immediately to set the initial position

    my_scheduled_function()
    
    # Schedule the function to be called at following times

    # schedule.every().day.at("09:00").do(my_scheduled_function)
    # schedule.every().day.at("11:30").do(my_scheduled_function)
    # schedule.every().day.at("15:00").do(my_scheduled_function)
    # schedule.every().day.at("21:40").do(my_scheduled_function)

    schedule.every(15).minutes.do(my_scheduled_function)

    while True:
        schedule.run_pending()
        time.sleep(1)

def my_scheduled_function():

    target_position = get_api_value()
    current_position = motor.get_position()    
    degrees_to_adjust = target_position - current_position

    if target_position > MAX_RANGE_OF_MOTER:
        log_the_output(datetime.now(), "Gage out of range. Not running motor to prefent damage to Robot.")
    else:
        log_the_output(datetime.now(), f"Ran the motor to position: {target_position} by turning {degrees_to_adjust} degrees")
        motor.run_for_degrees(degrees_to_adjust)

def get_api_value():
    
    achived_goal_degrees_value = 4755
    sum_donated_to_date = int(api_call())
    precent_achieved = int(sum_donated_to_date/SALES_GOAL * 100)
    api_value = int((achived_goal_degrees_value/100) * precent_achieved)
    return api_value

def log_the_output(date, message="No message was entered"):

    # Define the name of the logfile
  
    logfile = '/home/pi/Projects/givewp_glede/logs/log.csv'

    # Data to be written to the logfile
    data_to_log = {
        'timestamp': date.strftime('%Y-%m-%d %H:%M:%S'),
        'message': message
    }

    # Function to append data to the logfile
    def append_to_log(filename, data):
        # Check if the file exists and if it's empty to write headers
        try:
            file_empty = False
            with open(filename, 'r', newline='') as csvfile:
                file_empty = csvfile.read(1) == ''
        except FileNotFoundError:
            file_empty = True  # File does not exist, will be created

        # Open the file in append mode
        with open(filename, 'a', newline='') as csvfile:
            fieldnames = data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header if the file is empty
            if file_empty:
                writer.writeheader()

            # Write the data row
            writer.writerow(data)

    # Append new data to the logfile
    append_to_log(logfile, data_to_log)

def check_internet_connection(url='http://www.google.com', timeout=5):
    """Check for an internet connection by trying to fetch the specified URL."""
    try:
        # Perform a GET request to the specified URL
        response = requests.get(url, timeout=timeout)
        log_the_output(datetime.now(), "Connection to internet is confirmed")
        # If the request succeeds, return True
        return True
    except requests.ConnectionError:
        # If a connection error occurs, return False
        log_the_output(datetime.now(), "No internet connection available.")
        return False


if __name__ == '__main__':
    main()

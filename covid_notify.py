# importing required modules and libraries
# pip install requests
# pip install plyer
##https://www.javatpoint.com/desktop-notifier-in-python
import datetime # to read present date
import time # to suspend the execution for a specific time
import requests # to retrieve COVID stats from web
from plyer import notification # to get notification on the computer

# initializing a variable with None (temporary)
# indicating that there is no data available currently
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/usa")
except:

    print("cannot connet to the website, check internet connection")

# in case we fetched data
if (covidData != None):
    # converting data into JSON format
    jsonData = covidData.json()['Success']

    # repeating the loop for multiple times
    while(True):
        notification.notify(
            # defining the title of the notification,
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            # defining the message of the notification
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths : {todaydeaths}\nTotal active : {active}".format(
                        totalcases = jsonData['cases'],
                        todaycases = jsonData['todayCases'],
                        todaydeaths = jsonData['todayDeaths'],
                        active = jsonData["active"]),
            app_icon = "",
            # creating icon for the notification
            # we have to download a icon of ico file format
            #app_icon = '/Users/anup/python-workspace/python-practice/coronavirus.jpeg',
            # the notification stays for 30 seconds
            timeout  = 30
        )
        # sleep for 12 hrs => 60 * 60 * 12 seconds
        # notification repeats after every 12 hours
        time.sleep(60 * 60 * 12)
        #time.sleep(30)

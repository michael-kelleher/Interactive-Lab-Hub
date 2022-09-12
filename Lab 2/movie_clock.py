from __future__ import print_function
from time import strftime, sleep

import time
import datetime
import os.path

import pandas as pd
import random

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# while True:
#     print (strftime("%m/%d/%Y %H:%M:%S"), end="", flush=True)
#     print("\r", end="", flush=True)
#     sleep(1)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    df = pd.read_csv ('movies.csv')
    runtimes = marks_list = df['Runtime'].tolist()

    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        event = events_result.get('items', [])[0]

        if not event:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events

        start = event['start'].get('dateTime')
        #print("time until next event in minutes")

        dist = datetime.datetime.strptime(start[:-6], '%Y-%m-%dT%H:%M:%S')- datetime.datetime.now()
        minute = dist.seconds//60
        returnedTime = minute

        if minute > max(runtimes):
            returnedTime = max(runtimes)
        else:
            while returnedTime not in runtimes:
                returnedTime = returnedTime - 1
        options = df.loc[df['Runtime'] == returnedTime]

        if options.shape[0] == 1:
            ind = 0
        else:
            ind = random.randrange(options.shape[1])
        title = options["Title"].tolist()[ind]
        image = options["Image"].tolist()[ind]
        print(title, image)











    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':

    while True:
        main()

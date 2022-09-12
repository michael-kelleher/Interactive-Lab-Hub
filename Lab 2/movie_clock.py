from __future__ import print_function
from time import strftime, sleep

import time
import datetime
import os.path

import pandas as pd
import random
import requests
from io import BytesIO

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import digitalio
import board
from PIL import Image, ImageDraw
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():

    cs_pin = digitalio.DigitalInOut(board.CE0)
    dc_pin = digitalio.DigitalInOut(board.D25)
    reset_pin = digitalio.DigitalInOut(board.D24)

    # Config for display baudrate (default max is 24mhz):
    BAUDRATE = 24000000

    # Setup SPI bus using hardware SPI:
    spi = board.SPI()

    disp = st7789.ST7789(
        spi,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
        width=135,
        height=240,
        x_offset=53,
        y_offset=40,
    )

    if disp.rotation % 180 == 90:
        height = disp.width  # we swap height/width to rotate it to landscape!
        width = disp.height
    else:
        width = disp.width  # we swap height/width to rotate it to landscape!
        height = disp.height
    image = Image.new("RGB", (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
    disp.image(image)

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
        while True:
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
            ind = 0

            if options.shape[0] == 1:
                ind = 0
            else:
                ind = random.randrange(options.shape[1])
            title = options["Title"].tolist()[ind]
            imageURL = options["Image"].tolist()[ind]
            print(title, imageURL)

            response = requests.get(imageURL)

            image = Image.open(BytesIO(response.content))

            backlight = digitalio.DigitalInOut(board.D22)
            backlight.switch_to_output()
            backlight.value = True


            # Scale the image to the smaller screen dimension
            image_ratio = image.width / image.height
            screen_ratio = width / height
            if screen_ratio < image_ratio:
                scaled_width = image.width * height // image.height
                scaled_height = height
            else:
                scaled_width = width
                scaled_height = image.height * width // image.width
            image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

            # Crop and center the image
            x = scaled_width // 2 - width // 2
            y = scaled_height // 2 - height // 2
            image = image.crop((x, y, x + width, y + height))

            disp.image(image)
            sleep(2)











    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':

    main()

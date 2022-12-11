# Final Project  - Mirrorminders: I keep forgetting things!
Michael Kelleher
## Refresh from Project Plan
### Problem Statement
Life is busy, and the to-do lists pile up. Sometimes, it can be difficult to keep track of all the little things we are supposed to do. Building new habits, routines, and practices can just be hard to remember. Of course there are no shortage of solutions to this problem, but they all fall short. Phone apps are helpful, but they just add to our already too high screentime, lead to distraction, and can be cleared and reforgotten too easily. Writing everything down by hand can be tedious, too public, and far too easy to lose. 

### Exploration of Design Space
See below for some ideation of potential solutions
![IMG_1388](https://user-images.githubusercontent.com/90526300/201822599-1a7d6858-b7a1-4c86-938e-e765d3cf7e65.jpeg)
![IMG_1389](https://user-images.githubusercontent.com/90526300/201822602-bd4c8fa5-cceb-464a-9895-3a9eabb02208.jpeg)

![GF-Review-March-2020-21](https://user-images.githubusercontent.com/90526300/201822438-2d20b3fa-d4de-49a1-9208-4105bd10ba5d.jpg)
Inspiration drawn from this behind-the-mirror TV at Disney's Grand Floridian Hotel and Spa (Photo from https://worldofwalt.com/review-villa-grand-floridian-march-2020.html)

### Big Idea
Every day begins and ends in the same place, brushing your teeth in front of the bathroom mirror. This is the perfect time to reinforce important to-dos and reminders. After all, you have 2 minutes just staring at yourself! 

By placing a display behind the mirror, you'll be able to see a dynamic display with all this information, as well as other widgets like the weather or your daily schedule. It can integrate with your other devices so you can send new reminders from your phone whenever they come up throughout the day

To interact with the device in real time, it will utilize an IR frame to essentially turn the entire thing into a big touch screen. It can also use a gesture sensor to be woken up so that if you have guests over, they don't see your personal to-dos unless they very unusually start swiping at your bathroom mirror. 

## Design Process 
### A - Software Setup

The first key step was to create the display behind the mirror. This seemed like a relatively straightforward thing to code up as it should be a pretty static display with a few important API integrations. I began by making a basic display script, but quickly discovered there was an even easier way!

**MagicMirror<sup>2</sup>**
To my surprise, I found a suite of pre-built modular components that would solve a lot of what I was trying to build called MagicMirror<sup>2</sup>. 
https://magicmirror.builders/

I built out their default display which contained some relevant pieces like the NYT headlines and weather (albeit broken) and had a good start. This was a relatively straightforward process of downloading a few requirements, cloning their open source repo, and running it on my Raspberry Pi connected to a monitor. This tutorial was helpful for the initial setup: https://docs.magicmirror.builders/getting-started/installation.html

**Modules**

I then identified modules that would suit my needs. I chose to keep the default NYT headlines and weather from the default system, but I added 3 additional modules: MMM-MicrosoftToDO (https://github.com/thobach/MMM-MicrosoftToDo/), MMM-GoogleCalendar (https://github.com/randomBrainstormer/MMM-GoogleCalendar), and MMM-SmartTouch (https://github.com/EbenKouao/MMM-SmartTouch). The first module integrates with Microsoft's ToDo applicaion to create checklist items and track them across devices, the second does the same with google calendar events, and the last enables touch across the display when the IR frame is connected and adds menu items to turn off and restart the display.

**API Integrations**
Perhaps the most challenging componenet was working with Microsoft and Google's APIs and setting up proper authentication to get the data to sync properly. 
Microsoft specifically was difficult as the process had clearly changed since the last update of their documentation. First I went here: https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps to register a new Azure application, generate a client ID and secret key. You can then get an authorization key by tryng to access the application on an arbitrary local host and getting it from the response url. Finally the following code will return a response token, but you have to be fast or the authorization key will expire. You may also need to try a few times because the response can get cut off. 

    curl -X POST https://login.microsoftonline.com/common/oauth2/v2.0/token -H "Content-Type: application/x-www-form-urlencoded" -d       "grant_type=authorization_code&client_id=4ef19f40-4892-4905-b999-   76041e991f53&scope=offline_access%20user.read%20tasks.readwrite%20tasks.read&code=M30cd0dff-af91-d061-8755-ffb3b328aa03&redirect_uri=https%3A%2F%2Flocalhost%3A1234&client_secret=1Q25lsZTKEDf4RWBKVUbKjnaVuXytPaB"
    
With all those codes, keys, and tokens, the code was functional and the API integration was successful. 

Google was still a bit of a process, but the documentation was much clearer. This site was useful to get started: https://developers.google.com/calendar/api/quickstart/nodejs. You can hen set up your app, download a credentials file to the directory, and run the code as expected. 

OpenWeather was very simple. All I had to do was request a key here: https://openweathermap.org/ and input it into the code. 

**Finishing Touches**
Now that all the modules were working, my focused moved towards visual design. I chose to keep the color pallette very washed  out with only light white text. This was to ensure that the purpose of giving users a way to access this information without significant screen time was not overshadowed by basically turning the whole thing into a giant tablet. 

I also chose how to lay out the visual information. I put the time and date at the top left along with the to do list. As most people in the US scan from left to right, top to bottom, this seemed like a strong place to put the most important information. I then centered the calendar information on the top and put the weather to the right, as this was my expected hierarchyof information. I put the control buttons for on/off on the bottom center, indicated by a rectangle, and the NYT headlines below, as this was a nice-to-have but not essential bit of information, so I did not want it overly prominent. This is all managed in the config.js script.

<img width="1419" alt="Screen Shot 2022-12-10 at 7 02 47 PM" src="https://user-images.githubusercontent.com/90526300/206881209-574d4dc2-af02-4506-ba9b-f7ebe027613f.png">

The last bit of coding was setting the refresh rate. Becuase the typical user will be changing their calendar and to-dos throughout the day and not while actively using the device, I saw no reason to set up continuous API calls. Instead, it syncs once every 5 minutes, which should be more than enough. 

### B - Physical Design ###
In the ideal world, this would be mounted on a wall behind a bathroom mirror. As I was not going to do construction work on my rented apartment in the House, I chose to make a freestanding prototype instead

**The Display and Mirror**
The display part was easy. I used a 27" computer monitor that I already had to show the content. THe harder part was finding the right mirroring.  The most obvious choice was to buy a 1-way mirror, which is reflective from one side and transparent from the other. There were two issues here, the first was finding one of the appropriate dimensions, and the second was attaching it. I did not want to build a wood or metal frame to hold everything together sturdily, nor did I want to permanently attach it to my monitor. Similarly, even if I found or cut the correct dimensions, if I changed my mind on the display, I would have to start over again on the mirror. 

The display
![IMG_1551](https://user-images.githubusercontent.com/90526300/206881952-c3e9595a-52ed-4785-b473-3e7f9fead6b1.jpeg)



Instead, for prototyping purposes, I went to Home Depot and got Mirror Protective Film (like this https://www.amazon.com/Daytime-Privacy-Non-Adhesive-Decorative-Control/dp/B07P9Q4ZP8/ref=asc_df_B07P9Q4ZP8/?tag=hyprod-20&linkCode=df0&hvadid=385247960870&hvpos=&hvnetw=g&hvrand=13567255896448381332&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-846966847082&psc=1&tag=&ref=&adgrpid=81511522954&hvpone=&hvptwo=&hvadid=385247960870&hvpos=&hvnetw=g&hvrand=13567255896448381332&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9067609&hvtargid=pla-846966847082)
This solved a lot of my problems as it comes in a large roll that coud be easily cut to any size. It also has an adhesive on one side that can be easily taken off the display after I was done. 

Actually applying it was a bit of a challenge, as it would often stick to itself or get creases. I found the most succesful method was to lay it flat and then place the monitor on top of it face down. Then I used a blade to trim the eges and used a credit card to squeeze out as many of the air bubbles as possible. 

Test of applying the film
![IMG_1452](https://user-images.githubusercontent.com/90526300/206881968-0457e715-af2d-4426-a9be-027a6969ac73.jpeg)

First application of film
![IMG_1504](https://user-images.githubusercontent.com/90526300/206881957-a15c10fa-ce47-4803-bd25-731235434892.jpeg)

After Smooothing out air bubbles
![IMG_1505](https://user-images.githubusercontent.com/90526300/206881981-3a75daa5-54b4-41fd-865f-3d539bd80382.jpeg)


**The IR Frame**
In order to enable the touch features of turning the display on and off and crossing out to-do items, I needed an IR frame. I ordered one online (The actual item is no longer available, but this is similar, although significantly more expensive than the one I used https://www.amazon.com/dp/B082XRCQLZ?psc=1&ref=ppx_yo2ov_dt_b_product_details). I had to redownload drivers (included with the device) n order for it to work with the pi, but once that was set up, it was as simple as plugging it into the USB port and carefully positioning it to line up with the display. I used adhesive strips to mount it, and then it worked pretty well. 

The frame
![IMG_1506](https://user-images.githubusercontent.com/90526300/206881993-20c2a324-3898-41a5-9bfb-3fd48aa58d7d.jpeg)

Mounted
![IMG_1546](https://user-images.githubusercontent.com/90526300/206882209-b858d9a8-dfa4-4a67-ae87-0909d5e32c27.jpg)

**Costuming**
I was now left with a funky looking monitor/mirror. In order to make it look more like it would in a real context, I enclosed all of the framing and support stands in a simple cardboard box. I thought that jsut looked ugly, and given that this was meant to be a low-stress way of starting a day, I didn't like that. To fix this, I applied some wood grain contact paper to the outside to make it look more appealing. The pi and all the wire were simply placed on top of the monitor's support stand inside the box. 

The assembled box
![IMG_1526](https://user-images.githubusercontent.com/90526300/206882043-d94746fd-6549-4a56-bb1d-b0a62c4ed7f3.jpeg)

Cladded
![IMG_1549](https://user-images.githubusercontent.com/90526300/206882057-e6d530c1-e65d-4b69-b4b8-a9508fb51ec7.jpeg)
![IMG_1548](https://user-images.githubusercontent.com/90526300/206882069-c85bc25f-1e7a-4dbe-a82b-8f4c0b9d7481.jpeg)

Finished Device Running the program
![IMG_1533](https://user-images.githubusercontent.com/90526300/206882105-99e5ec07-2744-44c4-85fa-6e6039d24f3c.jpeg)

## User Testing and iteration
**Taken Feedback**
I asked a few of my friends to come over and try out the device. Some of the key feedback was that the visual display was pretty effective, but that they did not realize that the to-do's could be checked off. I went back into code to add the checkboxes next to the items and then people seemed to discover this more efficiently. I also increased the font size acrsoss the baord because people said it was challenging to read. 

**Rationale for Feedback Not Taken**
Other people commented that they didn't like that it only worked with Microsoft's to-do app because they use something different. I thought this was fair feedback, but I did not fix it as this was proof-of-concept and that would not enable significantly improved interaction. I also did not take the feedback for real-time refresh rates because I did not want to be putting in that many API calls and I do not think that outside of demo pruposes there is a real use case of standing at the bathroom mirror and updating your calendar on your phone. Lastly, people comented that the location for weather should update based on where you are phycially. Again, as this would be stationary in the real world, I did not find that to be a compelling use of effort. 

**Key Notes from In Class Demo**
A key note I picked up on when more people were using the device during the science fair style in-class demo day was that it was not obvious which features were touch enabled and what they could do. In future development I would want to add things to all modules like scrolling through the weather and calendar events or clicking on a headline to bring up more info. These would be based on watching users interact with the product, see what they want a touch to do, and then making that happen. Similarly, the square on/off button is not necessarily discoverable and perhaps some animation or a soft glow would be helpful in indicating that it can be pressed. 

However, people genuinely seemed to enjoy the project and understood how it could be used. They found the features generally useful and tought the mirror and touch were cool and interesting. 

People Using Device
![IMG_1535](https://user-images.githubusercontent.com/90526300/206882121-8d040ac5-c174-4bef-aa2a-24049c51e9e5.jpeg)
![IMG_1537](https://user-images.githubusercontent.com/90526300/206882124-165a3611-e44b-4ad4-8471-9466d002d2a7.jpeg)
![IMG_1538](https://user-images.githubusercontent.com/90526300/206882126-5a7da937-a229-4e2c-b9f6-62815f96eae8.jpeg)


## Video of Device in Action
https://user-images.githubusercontent.com/90526300/206881790-3b8ead75-ebd4-4455-90bb-5affcd5d3e58.mp4

Note that the film had begun peeling off quite badly by the time the video was filmed and I did not want to purchase new adhesive to attach the frame again, so I left it as is. 

## Reflections


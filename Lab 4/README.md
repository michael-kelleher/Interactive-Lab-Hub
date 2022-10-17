# Ph-UI!!!

**NAMES OF COLLABORATORS HERE**


For lab this week, we focus both on sensing, to bring in new modes of input into your devices, as well as prototyping the physical look and feel of the device. You will think about the physical form the device needs to perform the sensing as well as present the display or feedback about what was sensed. 

## Part 1 Lab Preparation

### Get the latest content:
As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. As we discussed in the class, there are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the personal access token for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab4 content"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

### Start brasinstorming ideas by reading: 
* [What do prototypes prototype?](https://www.semanticscholar.org/paper/What-do-Prototypes-Prototype-Houde-Hill/30bc6125fab9d9b2d5854223aeea7900a218f149)
* [Paper prototyping](https://www.uxpin.com/studio/blog/paper-prototyping-the-practical-beginners-guide/) is used by UX designers to quickly develop interface ideas and run them by people before any programming occurs. 
* [Cardboard prototypes](https://www.youtube.com/watch?v=k_9Q-KDSb9o) help interactive product designers to work through additional issues, like how big something should be, how it could be carried, where it would sit. 
* [Tips to Cut, Fold, Mold and Papier-Mache Cardboard](https://makezine.com/2016/04/21/working-with-cardboard-tips-cut-fold-mold-papier-mache/) from Make Magazine.
* [Surprisingly complicated forms](https://www.pinterest.com/pin/50032245843343100/) can be built with paper, cardstock or cardboard.  The most advanced and challenging prototypes to prototype with paper are [cardboard mechanisms](https://www.pinterest.com/helgangchin/paper-mechanisms/) which move and change. 
* [Dyson Vacuum Cardboard Prototypes](http://media.dyson.com/downloads/JDF/JDF_Prim_poster05.pdf)
<p align="center"><img src="https://dysonthedesigner.weebly.com/uploads/2/6/3/9/26392736/427342_orig.jpg"  width="200" > </p>

### Gathering materials for this lab:

* Cardboard (start collecting those shipping boxes!)
* Found objects and materials--like bananas and twigs.
* Cutting board
* Cutting tools
* Markers

(We do offer shared cutting board, cutting tools, and markers on the class cart during the lab, so do not worry if you don't have them!)

## Deliverables \& Submission for Lab 4

The deliverables for this lab are, writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do.
* "Acts like": shows how a person would interact with the device.

For submission, the readme.md page for this lab should be edited to include the work you have done:
* Upload any materials that explain what you did, into your lab 4 repository, and link them in your lab 4 readme.md.
* Link your Lab 4 readme.md in your main Interactive-Lab-Hub readme.md. 
* Group members can turn in one repository, but make sure your Hub readme.md links to the shared repository.
* Labs are due on Mondays, make sure to submit your Lab 4 readme.md to Canvas.


## Lab Overview

A) [Capacitive Sensing](#part-a)

B) [OLED screen](#part-b) 

C) [Paper Display](#part-c)

D) [Materiality](#part-d)

E) [Servo Control](#part-e)

F) [Record the interaction](#part-f)

## The Report (Part 1: A-D, Part 2: E-F)

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction 

We want to introduce you to the [capacitive sensor](https://learn.adafruit.com/adafruit-mpr121-gator) in your kit. It's one of the most flexible input devices we are able to provide. At boot, it measures the capacitance on each of the 12 contacts. Whenever that capacitance changes, it considers it a user touch. You can attach any conductive material. In your kit, you have copper tape that will work well, but don't limit yourself! In the example below, we use Twizzlers--you should pick your own objects.


<p float="left">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150" />
<img src="https://cdn-shop.adafruit.com/1200x900/4401-01.jpg" height="150">
</p>

Plug in the capacitive sensor board with the QWIIC connector. Connect your Twizzlers with either the copper tape or the alligator clips (the clips work better). In this lab, we will continue to use the `circuitpython` virtual environment we created before. Activate `circuitpython` and `cd` to your Lab 4 folder to install the requirements by:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" width=400>
These Twizzlers are connected to pads 6 and 10. When you run the code and touch a Twizzler, the terminal will print out the following

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python cap_test.py 
Twizzler 10 touched!
Twizzler 6 touched!
```

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" width=200>

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separated breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">
<img src="https://cdn-shop.adafruit.com/970x728/4991-01.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick

A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Distance Sensor

Earlier we have asked you to play with the proximity sensor, which is able to sense object within a short distance. Here, we offer [Qwiic Multi Distance Sensor](https://www.sparkfun.com/products/17072), which has a field of view of about 25° and is able to detect objects up to 3 meters away! 

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/0/3/4/17072-Qwiic_Multi_Distance_Sensor_-_VL53L3CX-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python distance_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_VL53L1X_Py) to learn more about the sensor and see other examples!

### Part C
### Physical considerations for sensing

Usually, sensors need to positioned in specific locations or orientations to make them useful for their application. Now that you've tried a bunch of the sensors, pick one that you would like to use, and an application where you use the output of that sensor for an interaction. For example, you can use a distance sensor to measure someone's height if you position it overhead and get them to stand under it.

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***

1. Automatc Blinds
This device automates the process of raising and lower blinds to adjust to the level of exterior light. It utilizes a light sensor to measure the incoming sunlight and than controls a servo to operate the blinds with that information.
2. Steering Wheel Safety
This device utilizes capacacative senors integrated into the steering wheel of a car in order to ensure that the driver's hands stay on the wheel. If they detect that the drvier is not holding the wheel, it will start beeping to alert them of the safety hazard. 
3. Garbage Can Overflow
It can be hard to remember to take out the trash because we forget when it is full. This devices places a proximity sensor on the inside of the trash can lid to measure how far from the to the trash line is. Then it puts a signifier on the front of the trash bin to let people know its time to empty the trash.
4. Hands free timer
When cooking, our hands are often dirty, so we can't operate a timer without washing our hands. Voice commands work, but not all of us want tohave something listening to us. This uses gesture controls to operate a wall mounted timer.
5. Park Assist
It can be hard to tell how close you are to a curb while parallel parking. This utilizes a proximity sensor to measure the distance and give visual feedback on the driver's dashboard.

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

1. Automatc Blinds
There need to be clear interactions to customize the threshholds for opening and closing as well as to turn the system on and off, perhaps on a daily schedule. This is not easy to accomplish with a physical user interface, and leans more heavily into an IOT framework operated by an app. That will need to be prototyped to understand what users would want to be able to do and waht feels intutive. Aesthetics will also be important to assess, as people may not want a bulky device on their walls. We will need to prototype sleek form factors to solve this. 
![IMG_1231](https://user-images.githubusercontent.com/90526300/195448446-7302f375-b1a9-471b-8875-56ce19fdcb9c.jpeg)

2. Steering wheel safety
This begs the question of what happens when a person is wearing gloves. do we want to be able to turn it on and off, or would that be abused? What are the threshholds for how long a driver should be able to have their hands off the wheel before an alert? Should it be triggered if just one hand is off the wheel? These questions are all safety related and need to be answered by experimenting with prototypes. Physically, we need to determine the proper placement for the capacitive sensors to ensure comfort and safety.
![IMG_1230](https://user-images.githubusercontent.com/90526300/195448536-0c87f45a-f486-4548-8f32-a0c6c5f91399.jpeg)


3. Garbage Can Overflow
THe big question is is there enough light inside a trashcan for the sensor to work, or do we need to add illumination and/or use an IR based sensor. That can be tested quickly with prototyping various designs. We also need to explore best notification systems. Do we want a small light on the front of the trashcan? An integration with a smartphone ping? Maybe a bigger screen on the trashcan? That neds to be explored with users
![IMG_1233](https://user-images.githubusercontent.com/90526300/195448570-8a02f1bb-88b8-4626-81e4-b81127b8f015.jpeg)


4. Hands free timer
It is not yet clear whether a wall mounted device or something that sits on the coutner and can be moved around is more ergonomic and provides more utility for users. It would be beneficial to try both options and get feedback on the prototypes. We also shoudl evaluate ways of dispalying the gesture information which are not obvious without some instructions.
![IMG_1232](https://user-images.githubusercontent.com/90526300/195448632-9b715f6f-2a10-4a53-81a3-ce771c0b7cf1.jpeg)


5. Park Assist
The placement of the sensor is key here, because it will likely have to be on an angle in order to actually see where the curb is. We will also need to explroe various housings for the sensor becuase the outside of a car is not a controleld environment and we need the sensor to reamin in place. This will need to be explored and stress tested. 
![IMG_1229](https://user-images.githubusercontent.com/90526300/195448671-06b3e9d5-2288-48c9-bf17-9571641206b2.jpeg)


**\*\*\*Pick one of these designs to prototype.\*\*\***


### Part D
### Physical considerations for displaying information and housing parts


Here is an Pi with a paper faceplate on it to turn it into a display interface:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/paper_if.png?raw=true"  width="250"/>


This is fine, but the mounting of the display constrains the display location and orientation a lot. Also, it really only works for applications where people can come and stand over the Pi, or where you can mount the Pi to the wall.

Here is another prototype for a paper display:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/b_box.png?raw=true"  width="250"/>

Your kit includes these [SparkFun Qwiic OLED screens](https://www.sparkfun.com/products/17153). These use less power than the MiniTFTs you have mounted on the GPIO pins of the Pi, but, more importantly, they can be more flexibily be mounted elsewhere on your physical interface. The way you program this display is almost identical to the way you program a  Pi display. Take a look at `oled_test.py` and some more of the [Adafruit examples](https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/tree/master/examples).

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/6/1/3/5/17153-SparkFun_Qwiic_OLED_Display__0.91_in__128x32_-01.jpg" height="200" />
<img src="https://cdn.discordapp.com/attachments/679466987314741338/823354087105101854/PXL_20210322_003033073.jpg" height="200">
</p>


It holds a Pi and usb power supply, and provides a front stage on which to put writing, graphics, LEDs, buttons or displays.

This design can be made by scoring a long strip of corrugated cardboard of width X, with the following measurements:

| Y height of box <br> <sub><sup>- thickness of cardboard</sup></sub> | Z  depth of box <br><sub><sup>- thickness of cardboard</sup></sub> | Y height of box  | Z  depth of box | H height of faceplate <br><sub><sup>* * * * * (don't make this too short) * * * * *</sup></sub>|
| --- | --- | --- | --- | --- | 

Fold the first flap of the strip so that it sits flush against the back of the face plate, and tape, velcro or hot glue it in place. This will make a H x X interface, with a box of Z x X footprint (which you can adapt to the things you want to put in the box) and a height Y in the back. 

Here is an example:

<img src="https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2020Fall/images/horoscope.png?raw=true"  width="250"/>

Think about how you want to present the information about what your sensor is sensing! Design a paper display for your project that communicates the state of the Pi and a sensor. Ideally you should design it so that you can slide the Pi out to work on the circuit or programming, and then slide it back in and reattach a few wires to be back in operation.
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

![IMG_1228](https://user-images.githubusercontent.com/90526300/195448810-49685113-6ad2-4977-828d-60a22a6f64cd.jpeg)

There are three versions of a standalone device with different configuarations of the sensor and the display. There are also three versions that are integrated into the kitchen environment. One is wall mounted on the backsplash. The second is built into the front of the counter. The final is built into the surface of a counter.

There are no buttons or knobs being used because the purpose of the device is to be hands free when a cook is busy with dirty hands. 

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

The three integrated versions call into question ergonomics. Is it easy to reach to the wall or is that difficult with the counter in the way? Is having it built into the front of the counter in too busy of an area that will get a lot of false signal? Is having it on top of the counter too likely to be covered by the work being done. THese questions will all need to be explored with real users in order to see how the physical design functions

THe standalone device is exploring  the most ergonomic arrangement of the sensor and display. It will be interesting to see how users place the device and use it. 

Between them all, the question is whether portability or consistent placement is more important to users. 

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

Portable device 1

**\*\*\*Explain the rationale for the design.\*\*\*** 

I'm most interested in the portable devices becuase people are often working in different parts of the kitchen and it could be useful to bring it with them. Also, I think the integrated designs are just a bigger commitment for users than something they can put away. 

The linear design of the sensor and display is the msot intutive as it does not require users to think about two sides of the device. To save space, I'm using the triangle design. 

While it is important that the device can be seen, kitchens are a releatively small space, and the user is most likely to be working nearby. Furthermore, kitchen real estate typically is at a premium. Thus, prioritizing a small form factor is important.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***
*Process*
First I cut a plan of the triangle box measured to have space inside for the raspberry  pi
![IMG_1241](https://user-images.githubusercontent.com/90526300/195467512-76476c3d-b70e-457e-9583-046b92178606.jpeg)
Next I folded it into place along the scores
![IMG_1243](https://user-images.githubusercontent.com/90526300/195467515-a26577c9-31d1-445a-a5d6-6ed9bd0d9527.jpeg)
I then cut hole for the display and sensor and drew the instructions
![IMG_1244](https://user-images.githubusercontent.com/90526300/195467517-35ae5d43-f057-4d13-af52-effd8e47a7cb.jpeg)
I then mounted the display and sensor inside
![IMG_1245](https://user-images.githubusercontent.com/90526300/195467520-1cc0c8dd-aec1-436e-9639-ab520595cb16.jpeg)
Rough prototype
![IMG_1246](https://user-images.githubusercontent.com/90526300/195467521-e7d2deda-68ad-4419-805e-21e84370265d.jpeg)
Inside of rough prototype
![IMG_1247](https://user-images.githubusercontent.com/90526300/195467522-4b6c1d15-d2d8-41e9-8797-022cd26b2d5f.jpeg)


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part E (Optional)
### Servo Control with Joystick

In the class kit, you should be able to find the [Qwiic Servo Controller](https://www.sparkfun.com/products/16773) and [Micro Servo Motor SG51](https://www.adafruit.com/product/2201). The Qwiic Servo Controller will need external power supply to drive, which are included in your kit. Connect the servo controller to the miniPiTFT through qwiic connector and connect the external battery to the 2-Pin JST port (ower port) on the servo controller. Connect your servo to channel 2 on the controller, make sure the brown is connected to GND and orange is connected to PWM.

<img src="Servo_Setup.jpg" width="400"/>

In this exercise, we will be using the nice [ServoKit library](https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython) developed by Adafruit! We will continue to use the `circuitpython` virtual environment we created. Activate the virtual environment and make sure to install the latest required libraries by running:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ pip3 install -r requirements.txt
```

A servo motor is a rotary actuator or linear actuator that allows for precise control of angular or linear position. The position of a servo motor is set by the width of an electrical pulse, that is, we can use PWM (pulse-width modulation) to set and control the servo motor position. You can read [this](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn a bit more about how exactly a servo motor works.

Now that you have a basic idea of what a servo motor is, look into the script `qwiic_servo_example.py` we provide. In line 14, you should see that we have set up the min_pulse and max_pulse corresponding to the servo turning 0 - 180 degree. Try running the servo example code now and see what happens:

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python servo_test.py
```

It is also possible to control the servo using the sensors mentioned in as in part A and part B, and/or from some of the buttons or parts included in your kit, the simplest way might be to chain Qwiic buttons to the other end of the Qwiic OLED. Like this:

<p align="center"> <img src="chaining.png"  width="200" ></p>

You can then call whichever control you like rather than setting a fixed value for the servo. For more information on controlling Qwiic devices, Sparkfun has several python examples, such as [this](https://learn.sparkfun.com/tutorials/qwiic-joystick-hookup-guide/all#python-examples).

We encourage you to try using these controls, **while** paying particular attention to how the interaction changes depending on the position of the controls. For example, if you have your servo rotating a screen (or a piece of cardboard) from one position to another, what changes about the interaction if the control is on the same side of the screen, or the opposite side of the screen? Trying and retrying different configurations generally helps reveal what a design choice changes about the interaction -- _make sure to document what you tried_!

### Part F
### Record

*Development*
Upon testing the first prototype while cooking with a few friends, there were a few important areas for future development:

https://user-images.githubusercontent.com/90526300/196258739-56d6124d-c851-422a-acf9-cb77d149cbf9.mp4


1. The gesture sensor was hard to ergonomically trigger when the device was far back on the counter because there was not space for the hand

https://user-images.githubusercontent.com/90526300/196258716-85b03887-9406-4d09-bfa4-541cda56c7f6.mp4


2. When it was closer to the front of the counter, it was recognizing a lot of false positives as you move around the kitchen.
3. Incrementing the time by 1 minute was very tedious, especially when trying to go from the default of 10 to something like 40 minutes. Given that this is more likely to be used for longer cooks than for short bursts (baking or raw meat is more likely to lead to dirty hands), the minute precision is less helpful than general long increments
4. There was no way to cancel the timer in the case of an error. This should be added. 
5. The sensor was not working well when behind the cardboard, likely because of light angles. I took the sensor out to the front of the housing. In future versions, a thinner material would likely be helpful

New Designs
I created three new physical form factor sketches. Two with more upright designs that solve the first two issues, allowing the device to be placed further back while leaving room for the hand. The triangle version is superior due to taking up less space and requiring less material, but it may not fit the pi on the inside without being too bulky. The third version hangs from overhead cabinets, but I chose not to use this one because it was less versatile for kitchens that may not have overhead cabinetry and requires it to be placed in a stationary position.

I then did 6 new sketched of the face design, focusing on clarity in instructions. After some ideation, I found a pretty straightforward option that should be intuitive for users. I will prototype that version to be sure. 
![IMG_1267](https://user-images.githubusercontent.com/90526300/196258881-ffc4e369-e046-46d4-9d58-519d90feb24b.jpg)



Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device


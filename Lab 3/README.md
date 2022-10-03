# Chatterboxes
**Independent Work**
[![Watch the video](https://user-images.githubusercontent.com/1128669/135009222-111fe522-e6ba-46ad-b6dc-d1633d21129c.png)](https://www.youtube.com/embed/Q8FWzLMobx0?start=19)

In this lab, we want you to design interaction with a speech-enabled device--something that listens and talks to you. This device can do anything *but* control lights (since we already did that in Lab 1).  First, we want you first to storyboard what you imagine the conversational interaction to be like. Then, you will use wizarding techniques to elicit examples of what people might say, ask, or respond.  We then want you to use the examples collected from at least two other people to inform the redesign of the device.

We will focus on **audio** as the main modality for interaction to start; these general techniques can be extended to **video**, **haptics** or other interactive mechanisms in the second part of the Lab.

## Prep for Part 1: Get the Latest Content and Pick up Additional Parts 

### Pick up Web Camera If You Don't Have One

Students who have not already received a web camera will receive their [IMISES web cameras](https://www.amazon.com/Microphone-Speaker-Balance-Conference-Streaming/dp/B0B7B7SYSY/ref=sr_1_3?keywords=webcam%2Bwith%2Bmicrophone%2Band%2Bspeaker&qid=1663090960&s=electronics&sprefix=webcam%2Bwith%2Bmicrophone%2Band%2Bsp%2Celectronics%2C123&sr=1-3&th=1) on Thursday at the beginning of lab. If you cannot make it to class on Thursday, please contact the TAs to ensure you get your web camera. 

### Get the Latest Content

As always, pull updates from the class Interactive-Lab-Hub to both your Pi and your own GitHub repo. There are 2 ways you can do so:

**\[recommended\]**Option 1: On the Pi, `cd` to your `Interactive-Lab-Hub`, pull the updates from upstream (class lab-hub) and push the updates back to your own GitHub repo. You will need the *personal access token* for this.

```
pi@ixe00:~$ cd Interactive-Lab-Hub
pi@ixe00:~/Interactive-Lab-Hub $ git pull upstream Fall2022
pi@ixe00:~/Interactive-Lab-Hub $ git add .
pi@ixe00:~/Interactive-Lab-Hub $ git commit -m "get lab3 updates"
pi@ixe00:~/Interactive-Lab-Hub $ git push
```

Option 2: On your your own GitHub repo, [create pull request](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2022Fall/readings/Submitting%20Labs.md) to get updates from the class Interactive-Lab-Hub. After you have latest updates online, go on your Pi, `cd` to your `Interactive-Lab-Hub` and use `git pull` to get updates from your own GitHub repo.

## Part 1.

### Text to Speech 

In this part of lab, we are going to start peeking into the world of audio on your Pi! 

We will be using the microphone and speaker on your webcamera. In the home directory of your Pi, there is a folder called `text2speech` containing several shell scripts. `cd` to the folder and list out all the files by `ls`:

```
pi@ixe00:~/text2speech $ ls
Download        festival_demo.sh  GoogleTTS_demo.sh  pico2text_demo.sh
espeak_demo.sh  flite_demo.sh     lookdave.wav
```

You can run these shell files by typing `./filename`, for example, typing `./espeak_demo.sh` and see what happens. Take some time to look at each script and see how it works. You can see a script by typing `cat filename`. For instance:

```
pi@ixe00:~/text2speech $ cat festival_demo.sh 
#from: https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)#Festival_Text_to_Speech

echo "Just what do you think you're doing, Dave?" | festival --tts
```

Now, you might wonder what exactly is a `.sh` file? Typically, a `.sh` file is a shell script which you can execute in a terminal. The example files we offer here are for you to figure out the ways to play with audio on your Pi!

You can also play audio files directly with `aplay filename`. Try typing `aplay lookdave.wav`.

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
(This shell file should be saved to your own repo for this lab.)

Bonus: If this topic is very exciting to you, you can try out this new TTS system we recently learned about: https://github.com/rhasspy/larynx

### Speech to Text

Now examine the `speech2text` folder. We are using a speech recognition engine, [Vosk](https://alphacephei.com/vosk/), which is made by researchers at Carnegie Mellon University. Vosk is amazing because it is an offline speech recognition engine; that is, all the processing for the speech recognition is happening onboard the Raspberry Pi. 

In particular, look at `test_words.py` and make sure you understand how the vocab is defined. 
Now, we need to find out where your webcam's audio device is connected to the Pi. Use `arecord -l` to get the card and device number:
```
pi@ixe00:~/speech2text $ arecord -l
**** List of CAPTURE Hardware Devices ****
card 1: Device [Usb Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```
The example above shows a scenario where the audio device is at card 1, device 0. Now, use `nano vosk_demo_mic.sh` and change the `hw` parameter. In the case as shown above, change it to `hw:1,0`, which stands for card 1, device 0.  

Now, look at which camera you have. Do you have the cylinder camera (likely the case if you received it when we first handed out kits), change the `-r 16000` parameter to `-r 44100`. If you have the IMISES camera, check if your rate parameter says `-r 16000`. Save the file using Write Out and press enter.

Then try `./vosk_demo_mic.sh`

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

### Serving Pages

In Lab 1, we served a webpage with flask. In this lab, you may find it useful to serve a webpage for the controller on a remote device. Here is a simple example of a webserver.

```
pi@ixe00:~/Interactive-Lab-Hub/Lab 3 $ python server.py
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 162-573-883
```
From a remote browser on the same network, check to make sure your webserver is working by going to `http://<YourPiIPAddress>:5000`. You should be able to see "Hello World" on the webpage.

### Storyboard

Storyboard and/or use a Verplank diagram to design a speech-enabled device. (Stuck? Make a device that talks for dogs. If that is too stupid, find an application that is better than that.) 

\*\***Post your storyboard and diagram here.**\*\*

![IMG_1193](https://user-images.githubusercontent.com/90526300/192305654-ef706492-c559-4088-aaa1-ecea251b1862.jpg)

\*\***Please describe and document your process.**\*\*

The goal of this device is to help actors memorize their lines (or anyone giving a presentation for that matter). First I though about the use case scenarios, and there really were two buckets: monologues and scenes. I started by working through the monologue UX as it is the simpler case. First, users would have to load in the script they were working from. Then once they start, the device listens along and keeps track of where they are in the script (with a high tolerance for errors with voice recognition). If the user says something very incorrect, the device will beep and read the first few words of the correct line. More commonly, if a user forgets their line and says "Line" the device will prompt them with the first few words of the next line. When it is complete, the system will read out some stats on how correct everything was. 

For scenes, this basic structure persists, but it also has a few additional augmentations. First, the device will ask the user which role they are playing and take the input. Then it will now read out each of the other roles in the scene, with different pre-assigned voices. It will also have a feature that if the user say a line when it is not their turn, it will also beep and then continue on.

See below for the flowchart


![Flowchart](https://user-images.githubusercontent.com/90526300/192308190-8bf20aca-bcdc-4104-997e-46fe692ce9fd.jpg)

### Acting out the dialogue

Find a partner, and *without sharing the script with your partner* try out the dialogue you've designed, where you (as the device designer) act as the device you are designing.  Please record this interaction (for example, using Zoom's record feature).

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

https://user-images.githubusercontent.com/90526300/192398859-319d0c1d-929a-4d55-b1de-b10dbbec409d.mp4

I tried a Wizard of Oz version of the interaction with my sister who has a lot of experience memorizing and acting. It went largely as expected, with her using the familiar cue of calling line to get input on the next phrase to say. It seemed rather intuitive and effective as a tool. One thing that was worth exploring was premptively offering line suggestions if the user is waiting a long time or saying "umm" because they may just not have remembered to call line. This would require significant further testing to ensure that it wasn't picking up on too many false positivies and jumping in with the answer too quickly.


### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*



# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...

I realized in the user testing that the corrections for misspoken lines were jsut too confusing and cumbersome to be useful. SImilalry, the different voices for the scene were distracting. The best interaction would be to simplify the process to just rely on calling "line" and give the prompt. A friend(Sarang) pointed out that if the word line was in the script, this would be a clear point of misunderstanding. This means that I should also add a feature where the script is first scanned for the word "line" and if it appears, not to count that as a signal. 

2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?

Perhaps an easier method for the interaction would be to have a button press when they want the prompt, but that would limit mobility and/or require actors to carry something around when their hands could be otherwise busy. For this reason, I think voice commands are the best method. In order to further clarify this, some simple messaging the costuming to remind the users of the command would be helpful. Additionally, it could eb good to display the text of the prompt to build up visual memory as well.

3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

***Attempt 1***
I tried to build a full solution that transcribed the text that it was hearing based on a full vocabulary. It would then compare that text to the target script to keep place. Then when prompted with "line," it would activate and read out the next 5 words. None of the systems we used in class were right for this becase I needed a more powerful transcription tool. I tried a few options such as these packages/tools:
https://github.com/petewarden/spchcat
https://linuxtut.com/en/1e044eb494623a3961a5/
https://forums.raspberrypi.com/viewtopic.php?t=27290
These worked to a variety of degrees but non provided me with the real time accruacy I needed in order to follow along with the target script. I think in the future, I would need to work with NLP models as well to get to a "close enough" level that would progress appropriately in order to make the tool actually useful. Without that, on missed word, an added um, a slight paraphrase, etc. render the tool useless.

***Attempt 2***
I further simplifed and went back to an expanded Wizard of Oz version of the tool. Now the device is just listening for the signal word: "Line." Upon hearing it, it triggers the human operator to type in the next five words and it then speaks that out loud. This provides a greater level of illusion that the tool is actually working than the version from Part 1 where the human operator did all parts. It also serves as proof of concept of the interaction technique in a realitvely robust way.

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

I tried the device with a few of my actor friends with monolgues they were working on either for class or auditions. 
Answer the following:

### What worked well about the system and what didn't?
It worked really well for the narrow use case of forgetting a line mid-practice session. It was natural and easy to call line and get the next few words. However, there were moments when it was less useful than a human helper, because 5 words for the prompt is arbitrary. Sometimes it would be more beneficial to give a longer phrase or a shorter phrase, but that is hard to codify into programmable rules. It also is entirely unhelpful for multi-purpose scenes, which is a huge component of memorization. 

### What worked well about the controller and what didn't?
The controller system worked quite well. It uses industry standard practices and felt natural to all participants. The key drawback here was the lack of ability to start at arbitrary points in a monologue or go back. Memorization is not always linear, so it is essential to be able to go back a couple lines and try again or not have to start from the beginning every time. 



### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?
1. The system really does need to support providing prompts of varying length depending on context. This will be difficult to program, but it is worth the consideration.
2. The system needs to be able to ignore filler words, track position in the speech less precisely, and deal with moderate paraphrasing. ALternatively, it needs to allow settings for level of prceision. If the actor is just trying to get the ideas, it should not require word perfect, but if they are trying to nail Shakespeare it is more reasonable. Regardless, the system needs to be able to figure out where an actor is in a monologue without limitations from poor speech to text tracking.
3. It needs to be a bit less of a black box. Users should be able to see what's happening (e.g. where the device thinks we are in the monologue) so they can see what's going wrong if necessary


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

This could be used to develop a dataset of commonly forgotten lines for acting teachers to help support with new memorization techniques and training. It could also be used to track usage of filler words, variations in speed (speaking too fast/slow), and otehr performance metrics to improve an actor's work. 


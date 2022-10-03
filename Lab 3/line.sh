espeak -ven+f2 -k5 -s150 --stdout "Welcome to What's My Line" | aplay

#arecord -f cd -r 441000 -d 5 -t wav recorded.wav && sox recorded.wav recorded_mono.wav remix 1,2

while true:
do
arecord -D hw:1,0 -f cd -c1 -r 48000 -d 5 -t wav recorded_mono.wav
res = python3 prompt.py recorded_mono.wav
read input
espeak -ven+f2 -k5 -s150 --stdout input | aplay

done

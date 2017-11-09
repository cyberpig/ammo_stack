# this is a is alarm clock program. it's was written in python 2 but now it's rewitten in py3 but it doesn't work work right
# now

import sys
import string
from time import sleep

sa = sys.argv
lsa = len(sys.argv)
if lsa != 2:
    print("Usage: [ python ] alarm_clock.py duration_in_minutes")
    print("Example: [ python ] alrm_clock.py 10")
    print("Use a value of 0 minutes for testing the alarm immediately.")
    print("Beeps a few times after the duration is over:")
    print("Press Crtl-C to terminate the alarm clock early.")
    sys.exit(1)

try:
    minutes = int(sa[1])
except ValueError:
    print("Invalid numric value (%s) for minutes") % sa[1]
    print("Should be an integer >= 0:")
    sys.exit(1)

seconds = minutes * 60

if minutes == 1:
    unit_word = " minute"
else:
    unit_word = "minutes"

try:
    if minutes > 0:
        print("Sleeping for ") + str(minutes) + unit_word
        sleep(seconds)
    print("Wake up")
    for i in range(5):
        print(chr(7))
        sleep(1)
except KeyboardInterrupted:
    print("Interrupted by user")
    sys.exit(1)

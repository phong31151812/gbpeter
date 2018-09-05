import snowboydecoder
import sys
import signal
interrupted = False
import os
import time
from event import Event as event
event().write("0")
def signal_handler(signal, frame):
    global interrupted
    interrupted = True
def interrupt_callback():
    interrupted = False
    return interrupted
def deteched():
    event().write("1")
    os.system("aplay {0}".format("resources/ding.wav"))
    while True:
        tu=event().read()
        if tu=="0":
            return False
        time.sleep(0.2)
model = ['/home/pi/AIY-projects-python/src/examples/voice/hello/hey.pmdl']
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
detector.start(detected_callback=deteched,interrupt_check=interrupt_callback,sleep_time=0.03)
detector.terminate()


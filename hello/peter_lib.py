import threading
class appshowing(threading.Thread):
    def __init__(self,kind,do):
        threading.Thread.__init__(self)
        self.kind=kind
        self.do=do
    def run(self):
        if self.kind=="User":
            os.system("sudo python3 ~/AIY-projects-python/src/examples/voice/integration/learningEnglish/Integration_User.py \" %s \" "%do)
        if self.kind=="Bot":
            os.system("sudo python3 ~/AIY-projects-python/src/examples/voice/integration/learningEnglish/Integration_Bot.py \" %s \" "%do)            
#-------------------------------------------------------------------------------------------------#
    
import logging
logging.basicConfig(level=logging.INFO,format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s")
import aiy.assistant.grpc
assist = [aiy.assistant.grpc.get_assistant(stt=0),aiy.assistant.grpc.get_assistant(stt=1),aiy.assistant.grpc.get_assistant(stt=2),aiy.assistant.grpc.get_assistant(stt=3),aiy.assistant.grpc.get_assistant(stt=4),aiy.assistant.grpc.get_assistant(stt=5),aiy.assistant.grpc.get_assistant(stt=6),aiy.assistant.grpc.get_assistant(stt=7),aiy.assistant.grpc.get_assistant(stt=8),aiy.assistant.grpc.get_assistant(stt=9),aiy.assistant.grpc.get_assistant(stt=10),aiy.assistant.grpc.get_assistant(stt=11)]
import aiy.audio
aiy.audio.get_recorder().start()


class voice_detech(object): 
    def __init__(self ,i):
        global assist
        self.assistant=assist[i]
        
    def get_data(self):
        text, audio = self.assistant.recognize()
        if text and audio:
            t1=appshowing("User",text)
            t1.start()
            return text, audio
        else:
            return None, None
        
#-------------------------------------------------------------------------------------------------#
        
import lib
hotword1=set(lib.hotword()[0])
hotword2=set(lib.hotword()[1])
hotword_reply=lib.hotword_reply()
class mining_hotword(object):
    def __init__(self,text):
        self.command=set(text.lower().split())
        self.text=text.lower()
    def run(self):
        if "your name" in self.text or "who're you" in self.text or "who are you" in self.text:
            return "name_ask_hot"
        global hotword1,hotword2
        if self.command & hotword1:
            if self.command & hotword2:
                return "wrong_name"
            return "name_find"
        return "name_not_find"

#-------------------------------------------------------------------------------------------------#

from textblob import TextBlob as tb
light1=set(lib.light_detech()[0])
light2 =set(lib.light_detech()[1])
light3 =set(lib.light_detech()[2])
animal1=set(lib.animal()[0])
animal2=set(lib.animal()[1])
emotion1=set(lib.emotion_detech()[0])
emotion2=set(lib.emotion_detech()[1])
emotion_reply=lib.emotion_reply()
fat=lib.father()
fatw=lib.where()
class mining_text(object):
    def __init__(self,text):
        self.command=set(text.lower().split())
        self.text=text.lower()
    def run(self):
        global light1,light2,light3,emotion1,emotion2,animal1,animal2,fat
        if self.text == "hello peter" or self.text == "hello peter":
            return "hi"
        if self.text in fat:
            return "father"
        if self.text in fatw:
            return "where"
        if self.command & light1:
            if self.command & light3:
                tu=self.command & light2
                tu=' '.join(tu)
                tu="light"+tu
                return tu
        if self.command&emotion1:
            if self.command&emotion2:
                tu=self.command&emotion1
                tu =' '.join(tu)
                tu=tb(tu).correct()
                tu=float(tu.sentiment.polarity)
                if tu > 0.2:
                    return "happy"
                elif (tu <= 0.2) & (tu>=-0.2):
                    return "normal"
                elif tu<-0.2:
                    return "angry"
        if "your name" in self.text or "who're you" in self.text or "who are you" in self.text:
            return "name_ask"
        if set(["hand","hands"])&self.command and set(["right","left","both"])& self.command and set(["up","down"])&self.command:
            tu = set(["right","left","both"]) & self.command
            tu =' '.join(tu)
            tu1= set(["up","down"])&self.command
            tu1=' '.join(tu1)
            tu2= tu + " hand " + tu1
            return tu2
        if set(["go","turn","move","roll","turn"])&self.command and set(["ahead","forward","back","backward","left","right"])&self.command:
            tu = set(["go","turn","move","roll","turn"]) & self.command
            tu =' '.join(tu)
            tu1= set(["ahead","forward","back","backward","left","right"])&self.command
            tu1=' '.join(tu1)
            tu2= tu + " " + tu1
            if tu2 in self.text:
                if set([tu2])&set(["go ahead","go forward","move ahead","move forward"]):
                    return "ahead"
                if set([tu2])&set(["move back","go back","roll back","go backward","move backward","roll backward"]):
                    return "back"
                if set([tu2])&set(["turn left"]):
                    return "left_turn"
                if set([tu2])&set(["turn right"]):
                    return "right_turn"
        return "other"
#-------------------------------------------------------------------------------------------------#
import random as rd
import os
import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
'''
R_pin=5
B_pin=12
G_pin=24
gpio.setup(R_pin,gpio.OUT)
gpio.setup(B_pin,gpio.OUT)
gpio.setup(G_pin,gpio.OUT)
Rp=gpio.PWM(R_pin,80)
Bp=gpio.PWM(B_pin,80)
Gp=gpio.PWM(G_pin,80)'''

pin_phai_tien = 4
pin_phai_lui = 17
pin_trai_tien = 27
pin_trai_lui = 22
gpio.setup(pin_phai_tien, gpio.OUT)
gpio.setup(pin_phai_lui, gpio.OUT)
gpio.setup(pin_trai_tien, gpio.OUT)
gpio.setup(pin_trai_lui , gpio.OUT)
gpio.output(pin_phai_tien, 0)
gpio.output(pin_phai_lui, 0)
gpio.output(pin_trai_tien, 0)
gpio.output(pin_trai_lui, 0)

from servo import *
pin_tay_trai=26
pin_tay_phai=6
pin_dau=13
servo_tay_trai = servo(pin_tay_trai)
servo_tay_phai = servo(pin_tay_phai)
servo_dau = b_servo(pin_dau)
hand_trai_nor=0
hand_trai_haf=90
hand_trai_max=180
hand_trai=hand_trai_nor
hand_phai_nor=180
hand_phai_haf=90
hand_phai_max=0
hand_phai=hand_phai_nor
head_nor=110
head_min=70
head_max=160
head=head_nor
servo_tay_trai.ride(hand_trai_nor)
print("handtrai")
servo_tay_phai.ride(hand_phai_nor)
print("handphai")
servo_dau.ride(head_nor)
print("head")

threadLock = [threading.Lock(),threading.Lock()]

class motor(threading.Thread):
    def __init__(self,kind,lock=-1,do=0,timer=0):
        threading.Thread.__init__(self)
        self.kind=kind
        self.lock=lock
        self.do=do
        self.timer=timer
    def run(self):
        print("start %s" % (self.kind))
        if self.lock==-1:
            pass
        else:
            threadLock[self.lock].acquire()
        '''if self.kind=="light on":
            self.light_start()
        elif self.kind=="light off":
            self.light_off()
        elif self.kind=="angry":
            self.light_start()
            for i in range(0,101,5):
                self.light(100,100-i,100-i)
                time.sleep(0.03)
            time.sleep(1)
            for i in range(0,101,5):
                self.light(100,i,i)
                time.sleep(0.03)
            self.light_stop()
        elif self.kind=="normal":
            self.light_start()
            for i in range(0,101,5):
                self.light(100-i,100,100-i)
                time.sleep(0.03)
            for i in range(0,101,5):
                self.light(i,100,i)
                time.sleep(0.03)
            self.light_stop()'''
        if self.kind=="head":
            self.head(self.do,self.timer)
        elif self.kind=="right_hand":
            self.right_hand(self.do,self.timer)
        elif self.kind=="left_hand":
            self.left_hand(self.do,self.timer)
        elif self.kind=="ahead":
            self.move(1,0,1,0)
        elif self.kind=="back":
            self.move(0,1,0,1)
        elif self.kind=="left_turn":
            self.move(1,0,0,1)
        elif self.kind=="right_turn":
            self.move(0,1,1,0)    
        if self.lock==-1:
            pass
        else:
            threadLock[self.lock].release()
        print("stop %s" % (self.kind))

    '''def light_start(self):
        global Rp, Bp,Gp
        Rp.start(100)
        Bp.start(100)
        Gp.start(100)
        
    def light(self,R,B,G):
        global Rp,Bp,Gp
        Rp.ChangeDutyCycle(R)
        Gp.ChangeDutyCycle(G)
        Bp.ChangeDutyCycle(B)
        
    def light_stop(self):
        global Rp, Bp,Gp
        Rp.stop()
        Bp.stop()
        Gp.stop()'''

    def head(self,do,timer=0):
        global head, servo_dau, pin_dau
        gpio.setup(pin_dau,gpio.OUT)
        servo_dau.ride(do,head,timer)
        head=do
        print("a")

    def right_hand(self,do,timer=0):
        global hand_phai, servo_tay_phai, pin_tay_phai
        gpio.setup(pin_tay_phai,gpio.OUT)
        servo_tay_phai.ride(do,hand_phai,timer=0)
        hand_phai = do
        print("a")
        
    def left_hand(self,do,timer=0):
        global hand_trai, servo_tay_trai, pin_tay_trai
        gpio.setup(pin_tay_trai,gpio.OUT)
        servo_tay_trai.ride(do,hand_trai,timer=0)
        hand_trai = do
        print("a")

    def move(self,phai_tien=0,phai_lui=0,trai_tien=0,trai_lui=0):
        global pin_phai_tien,pin_phai_lui,pin_trai_tien,pin_trai_lui
        gpio.output(pin_phai_tien, phai_tien)
        gpio.output(pin_phai_lui, phai_lui)
        gpio.output(pin_trai_tien, trai_tien)
        gpio.output(pin_trai_lui, trai_lui)
        time.sleep(2)
        gpio.output(pin_phai_tien, 0)
        gpio.output(pin_phai_lui, 0)
        gpio.output(pin_trai_tien, 0)
        gpio.output(pin_trai_lui, 0)
        

    
class job_event(object):
    def __init__(self,event,text=None,audio=None):
        self.event=event
        self.text=text
        self.audio=audio
    def run(self):
        if self.event=="name_ask_hot":
            t="I'm Peter pot. If you want to ask me anything. Please call my name."
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="name_find":
            global hotword_reply
            t=hotword_reply[rd.randint(0,len(hotword_reply)-1)]
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="name_not_find":
            t="You said: "+ self.text + ". Please call my name."
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="wrong_name":
            t="Not Peter Pan. I'm Peter pot. You can Call me Peter."
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="name_ask":
            t="I'm Peter Pot. You can Call me Peter."
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="name_again":
            t="My name again,please."
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return 
        '''if self.event=="hi":
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="father":
            aiy.audio.say("GB Innovation, vietnam")
            return
        if self.event=="where":
            aiy.audio.say("ajou university, sound korea")
            return
        if self.event=="light on":
            self.light_start()
            return
        if self.event=="light off":
            self.light_stop()
            return'''
        if self.event =="angry":
            #light = motor("angry")
            global emotion_reply,head_max,head_min,head_nor
            head = motor("head",0,head_max,0.25)
            head1 = motor("head",0,head_min,0.5)
            head2 = motor("head",0,head_nor,0.5)
            head.start()
            time.sleep(0.01)
            head1.start()
            time.sleep(0.01)
            head2.start()
            #light.start()
            t= emotion_reply[0][rd.randint(0,len(emotion_reply[0])-1)]
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        '''if self.event =="normal":
            light = motor("normal")
            light.start()
            global emotion_reply
            aiy.audio.say(emotion_reply[1][rd.randint(0,len(emotion_reply[1])-1)])
            return'''
        if self.event =="happy":
            global emotion_reply,hand_phai_max,hand_phai_nor
            han= motor("right_hand",0,hand1_max)
            han1 = motor("right_hand",0hand1_nor)
            han.start()
            time.sleep(0.01)
            han1.start()
            t= emotion_reply[2][rd.randint(0,len(emotion_reply[2])-1)]
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event == "right hand up":
            global hand_phai,hand_phai_nor,hand_phai_haf,hand_phai_max
            if hand_phai==hand_phai_nor:
                hand= motor("right_hand",-1,hand_phai_haf)
                hand.start()
            else:
                hand= motor("right_hand",-1,hand_phai_max)
                hand.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event == "right hand down":
            global hand_phai_nor
            hand= motor("right_hand",-1,hand_phai_nor)
            hand.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event == "left hand up":
            global hand_trai,hand_trai_nor,hand_trai_haf,hand_trai_max
            if hand_trai==hand_trai_nor:
                hand= motor("left_hand",-1,hand_trai_haf)
                hand.start()
            else:
                hand= motor("left_hand",do=hand_trai_max)
                hand.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event == "left hand down":
            global hand_trai_nor
            hand= motor("left_hand",do=hand_trai_nor)
            hand.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event == "both hand down":
            global hand_trai_nor,hand_phai_nor
            hand= motor("right_hand",do=hand_trai_nor)
            hand1= motor("left_hand",do=hand_phai_nor)
            hand.start()
            hand1.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event == "both hand up":
            global hand_phai_max,hand_trai_max
            hand= motor("right_hand",-1,hand_phai_max)
            hand1= motor("left_hand",-1,hand_trai_max)
            hand.start()
            hand1.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event == "right_turn" or self.event == "left_turn" or self.event == "back" or self.event == "ahead":
            mot=motor(self.event)
            mot.start()
            t="Done"
            t2=appshowing("Bot",t)
            t2.start()
            return
        if self.event=="back_to_hey":
            t="Say \"Hey\" again, please"
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="other":
            global assist
            t="Data from internet"
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.play_audio(self.audio,volume=100)
            return
        if self.event=="not":
            t="Are you saying anything?"
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return
        if self.event=="reset":
            t="I am ready."
            t2=appshowing("Bot",t)
            t2.start()
            aiy.audio.say(t)
            return

 
     
    

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
gioihan=0.001
class servo:
    'Dieu khien servo'
    frequency = 50

    def __init__(self, PinGPIO):
        self.PinGPIO = PinGPIO
        
        
    def ride(self, angle,ang_cur=-1,timer=0):
        GPIO.setup(self.PinGPIO, GPIO.OUT)
        self.pwm = GPIO.PWM(self.PinGPIO, servo.frequency)
        self.pwm.start(2.5)
        if ang_cur==-1:
            DC = 1./22.*angle + 2.5
            self.pwm.ChangeDutyCycle(DC)
            time.sleep(0.5)
        else:
            a1=timer/abs(angle-ang_cur)
            if a1<0.001:
                a1=0.001                
            DC = 1./22.*angle + 2.5
            t= 1./22.*ang_cur + 2.5
            sta=time.time()
            while (t*1000000//1)!=(DC*1000000//1):
                if t<DC:
                    t+=1/22*1
                    self.pwm.ChangeDutyCycle(t)
                    time.sleep(a1)
                else:
                    t-=1/22*1
                    self.pwm.ChangeDutyCycle(t)
                    time.sleep(a1)
            sta=(time.time()-sta)
            print(sta)
        GPIO.cleanup(self.PinGPIO)
        
class b_servo:
    'Dieu khien servo'
    frequency = 50

    def __init__(self, PinGPIO):
        self.PinGPIO = PinGPIO
        
        
    def ride(self, angle,ang_cur=-1,timer=0):
        GPIO.setup(self.PinGPIO, GPIO.OUT)
        self.pwm = GPIO.PWM(self.PinGPIO, servo.frequency)
        self.pwm.start(2.5)
        if ang_cur==-1:
            DC = 1./22.*angle + 2.5
            self.pwm.ChangeDutyCycle(DC)
            time.sleep(0.5)
        else:
            a1=timer/abs(angle-ang_cur)
            if a1<0.001:
                a1=0.001                
            DC = 1./25.*angle + 2.5
            t= 1./25.*ang_cur + 2.5
            sta=time.time()
            while (t*1000000//1)!=(DC*1000000//1):
                if t<DC:
                    t+=1/25*1
                    self.pwm.ChangeDutyCycle(t)
                    time.sleep(a1)
                else:
                    t-=1/25*1
                    self.pwm.ChangeDutyCycle(t)
                    time.sleep(a1)
            sta=(time.time()-sta)
            print(sta)
        GPIO.cleanup(self.PinGPIO)

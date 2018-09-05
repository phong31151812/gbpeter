from servo import *
import time as a
pin_tay_trai=26
servo_tay_trai = servo(pin_tay_trai)
t=90
a=time.time()
servo_tay_trai.ride(angle=t)
a1=time.time()
print("a= ",a1-a)
cur=45
a=time.time()
servo_tay_trai.ride(cur,t)
a1=time.time()
print("a= ",a1-a)
t=cur
cur=135
a=time.time()
servo_tay_trai.ride(cur,t)
a1=time.time()
print("a= ",a1-a)
t=cur
cur=90
a=time.time()
servo_tay_trai.ride(cur,t)
a1=time.time()
print("a= ",a1-a)

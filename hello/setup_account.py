#!/usr/bin/env python3
import logging
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import os
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

def main():
    acc=input('nhap so luong acc:')
    acc=int(acc)
    aiy.audio.get_recorder().start()
    for i in range(acc):
        t= os.path.expanduser('~/acc')
        if not os.path.exists(t):
             os.mkdir(t)
        t1=str(i)+'.json'
        link= os.path.join(t,t1)
        if not os.path.exists(link):
             print('khong co file %s.json'%i)
             break
        print("test file %s >>>"%i)
        assistant = aiy.assistant.grpc.get_assistant(link=link,stt=i)
        text, audio = assistant.recognize()
        if text:
            print('text ok')
        if audio:
            print('audio ok')
        if i==acc-1:
            o=open('acc_count','w')
            o.write(str(acc))
    
if __name__ == '__main__':
    main()

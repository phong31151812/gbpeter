#!/usr/bin/python3
import sys
userTalk = sys.argv[1]
print("1")
from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
    socketIO.emit('Learning_English', 'user:' + userTalk)
    socketIO.wait(seconds=1)

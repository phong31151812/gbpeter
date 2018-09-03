#!/usr/bin/python
import sys
userTalk = sys.argv[1]
machineTalk = sys.argv[2]

from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
    socketIO.emit('Learning_English', userTalk + ';;;' + machineTalk)
    socketIO.wait(seconds=1)
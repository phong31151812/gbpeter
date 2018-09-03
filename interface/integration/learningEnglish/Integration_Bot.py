#!/usr/bin/python3
import sys
botTalk = sys.argv[1]

from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
    socketIO.emit('Learning_English', 'bot:' + botTalk)
    socketIO.wait(seconds=1)

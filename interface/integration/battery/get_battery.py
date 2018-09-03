#!/usr/bin/python
import sys
# Value: 0,25,50,75,100
battery = sys.argv[1]

from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 1000, LoggingNamespace) as socketIO:
    socketIO.emit('Learning_English', 'battery:' + battery)
    socketIO.wait(seconds=1)

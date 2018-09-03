#!/usr/bin/python
import sys
# Value: 0-100
volume = sys.argv[1]

from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
    socketIO.emit('Learning_English', 'volume:' + volume)
    socketIO.wait(seconds=1)

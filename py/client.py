import logging
from socketIO_client import SocketIO, LoggingNamespace

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
    socketIO.emit('chat message', 'hello from python')

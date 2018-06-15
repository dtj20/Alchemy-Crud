"""
simple server application for recieveing messages
"""
import socket
import threading
import time

class ListenServer(object):
    """
    ListenServer recieves messages to be passed on to the application
    """

    def __init__(self, message_queue, conf_dict):
        """
        init method sets the message queue and the configuration_dictionary
        """
        self.message_queue = message_queue
        self.port = conf_dict['server']['port']
        self.listen = True
        self.create_server()
        self.start_listener()

    def create_server(self):
        """
        creates a server for recieveing messages
        """
        self.socket = socket.socket()
        self.socket.connect(('localhost', self.port))

    def start_listener(self):
        """
        start_listener will fire up a listen server on a seperate thread
        """
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()

    def listen(self):
        """
        listen will sit in a threaded loop adding messages to the message_queue
        """
        while self.listen:
            data = s.recv(1024)
            time = time.time()
            tup = (time, data)
            self.message_queue.put(tup)

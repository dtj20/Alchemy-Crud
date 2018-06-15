"""
main point for application. Holds the main class
"""
from config_reader import ConfigReader
from server import ListenServer
from alchemy import SqlAlchemy
import Queue

class main(object):
    """
    main class for the program holds the init method for entry
    """

    def __init__(self):
        """
        initi method creates the required files and locations
        """
        message_queue = Queue.Queue()
        conf_reader = ConfigReader()
        configuration_dictionary = conf_reader.conf_dict
        listen_server = ListenServer(message_queue, configuration_dictionary)
        sql_alchemy = SqlAlchemy(configuration_dictionary)



if __name__ == "__main__":
    main()

"""
main point for application. Holds the main class
"""
from config_reader import ConfigReader

class main(object):
    """
    main class for the program holds the init method for entry
    """

    def __init__(self):
        """
        initi method creates the required files and locations
        """
        ConfigReader()
        print "1"


if __name__ == "__main__":
    main()

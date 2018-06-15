"""
logging wrapper. Creates a custom logger, must be setup in main
"""

def setup_custom_logger(message_level):
    """
    setup_custom_logger creates a logger with a supplied debug level
    """

    name = 'alchemy-logger'
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def get_logger():
    """
    returns the current defined logger.
    """
    logger = logging.getLogger('alchemy-logger')
    return logger

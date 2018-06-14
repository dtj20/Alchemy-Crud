"""
config_reader reads the values from alchemy.conf as a dictionary
on startup.
"""

import configparser

class ConfigReader(object):
    """
    reads the configuration object and exports the data to a dictionary
    """

    conf_dict = {}

    def __init__(self):
        """
        init method for the application
        """
        self.config_reader = configparser.ConfigParser()
        self.load_config("alchemy.conf")
        self.read_sections()

    def load_config(self, config_name):
        """
        loads the configuration file into memory
        """
        self.config_reader.read(config_name)

    def read_sections(self):
        """
        reads the sections in the supplied config and creates the
        dictionaries
        """
        sections = self.config_reader.sections()
        for section in sections:
            self.read_section(section)

    def read_section(self, section):
        """
        reads each section and loads the data into a dictionary
        """
        section_dict = {}
        keys = self.config_reader.options(section)
        values = []
        for key in keys:
            value = self.config_reader.get(section, key)
            values.append(value)

        for key, value in zip(keys, values):
            section_dict[key] = value
        self.conf_dict[section] = section_dict

"""
alchemy class page. handles the main interaction with sqlAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from consist_now import Consist_Now


class SqlAlchemy(object):
    """
    The sqlAlchemy class. creates a database connection on startup
    """

    def __init__(self, conf_dict):
        """
        init method for sql alchemey.
        """
        self.conf_dict = conf_dict
        self.create_engine()
        self.create_session()
        self.get_consist_now()

    def create_engine(self):
        """
        creates the engine that connects to the database
        """
        recyc_time = self.conf_dict['database']['recyc_time']
        database_type = self.conf_dict['database']['database_type']
        user = self.conf_dict['database']['user']
        password = self.conf_dict['database']['password']
        host = self.conf_dict['database']['host']
        database = self.conf_dict['database']['database_name']
        if database_type in "mysql":
            connect_string = 'mysql+pymysql://%s:%s@%s/%s' % (user, password, host, database)
            self.engine = create_engine(connect_string)

    def create_session(self):
        """
        creates a session. the factory that links to the database
        """
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def remove_table_entry(self, instance):
        """
        method that removes an item from the table
        """
        self.session.delete(instance)

    def add_table_entry(self, instance):
        """
        method to add an entry to the table
        """
        self.session.add(instance)

    def batch_remove_table_entries(self, rem_list):
        """
        removes a batch of table entries from the table
        """
        for entry in rem_list:
            self.remove_table_entry(entry)

    def batch_add_table_entries(self, add_list):
        """
        adds a batch of table entries to the table
        """
        for entry in add_list:
            self.add_table_entry(entry)

    def commit(self):
        """
        commits changes to the database
        """
        self.session.commit()

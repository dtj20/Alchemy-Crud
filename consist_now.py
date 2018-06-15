"""
ORM file for a mysql table
"""

from sqlalchemy import Column, BigInteger, Integer, String, Text, VARCHAR
from alchemy import Base
class Consist_Now(Base):
    """
    Consist Table ORM maps the consist_now table to a class
    """

    __tablename__ = 'consist_now'

    tstamp_ccu = Column(BigInteger)
    tstamp_rcvd = Column(BigInteger)
    fleet = Column(VARCHAR)
    location_ref = Column(VARCHAR)
    location_sub_ref = Column(VARCHAR)
    carriage_idx = Column(Integer)
    mac_address = Column(VARCHAR, primary_key=True)
    ip_address = Column(VARCHAR)
    peer = Column(VARCHAR)
    peer1 = Column(VARCHAR)
    peer2 = Column(VARCHAR)
    sys_desc = Column(Text)

    def __repr__(self):
        """
        creates a formatted Consist_Now object
        """
        return ("<Consist_Now(tstamp_ccu='%s', tstamp_rcvd='%s', fleet='%s',"
               "location_ref='%s', location_sub_ref='%s', carriage_idx='%s',)"
               "mac_address='%s', ip_address='%s', peer='%s', peer1='%s',"
               "peer2='%s', sys_desc='%s')>") % (self.tstamp_ccu, self.tstamp_rcvd,
               self.fleet, self.location_ref, self.location_sub_ref, self.carriage_idx,
               self.mac_address, self.ip_address, self.peer, self.peer1, self.peer2,
               self.sys_desc)

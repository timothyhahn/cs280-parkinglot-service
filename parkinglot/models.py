from sqlalchemy import Column, Integer, String, Text, Float
from database import Base


class ParkingLot(Base):
    __tablename__ = 'parkinglot'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    pricing = Column(Text)
    hours = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, name=None, pricing=None, hours=None, latitude=None, longitude=None):
        self.name = name
        self.pricing = pricing
        self.hours = hours
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<Lot %r>' % (self.name)

    def info(self):
    	lot_dict = dict()
    	lot_dict['id'] = self.id
    	lot_dict['name'] = self.name
    	lot_dict['pricing'] = self.pricing
    	lot_dict['hours'] = self.hours
    	lot_dict['longitude'] = self.longitude
    	lot_dict['latitude'] = self.latitude
    	return lot_dict

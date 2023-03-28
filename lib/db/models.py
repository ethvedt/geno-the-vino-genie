from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint,  Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///vino_geno.db', echo=True)

Base = declarative_base()

class Meal(Base):
    __tablename__  = 'meal'
    __tableargs__ = (PrimaryKeyConstraint('id'),)

    # has meat base -> boolean
    # meat type -> str
    # is vegetable base -> boolean
    # fruits -> str
    # is grain base -> boolean
    # food region -> str
    # flavor profile -> str

    id = Column(Integer())
    has_meat = Column(Boolean())
    meat_type = Column(String())
    veg_type = Column(String())
    region = Column(String())
    flavor_profile = Column(String())


    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'has meat: {self.has_meat}, ' + \
            f'meat type: {self.meat_type}', + \
            f'veg type: {self.veg_type}', + \
            f'region: {self.region}, ' + \
            f'flavor profile: {self.flavor_profile}'
    

class Wine(Base):
    __tablename__  = 'wine'
    __tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    grape_varietal = Column(String())
    region  = Column(String())

    meals = relationship('Meal', backref=backref('meal') )

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'grape varietal: {self.grape_varietal}, ' + \
            f'region: {self.region}'
    


class WineMeals(Base):
    __tablename__  = 'wine_meal'
    __tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer())
    meal_id = Column(Integer(), ForeignKey('meals.id'))
    wine_id = Column(Integer(), ForeignKey('wines.id'))

    meal = relationship('Meal', backref=backref('meal'))
    wine = relationship('Wine', backref=backref('wine'))

    def __repr__(self):
        return f'wine meal id: {self.id}, ' + \
            f'meal id: {self.meal_id}, ' + \
            f'region: {self.wine_id}'


from sqlalchemy import create_engine
from sqlalchemy import PrimaryKeyConstraint,  Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///vino_geno.db', echo=True)

Base = declarative_base()

class Meal(Base):
    __tablename__  = 'meals'
    #__tableargs__ = (PrimaryKeyConstraint('id'),)

    # has meat base -> boolean
    # meat type -> str
    # is vegetable base -> boolean
    # fruits -> str
    # is grain base -> boolean
    # food region -> str
    # flavor profile -> str

    wine_meal = relationship('WineMeals', backref=backref('meal'))

    id = Column(Integer(),  primary_key=True)
    name = Column(String())
    meat_type = Column(String())
    veg_type = Column(String())
    flavor_profile = Column(String())
    starch_profile = Column(String())
    spice_profile = Column(String())
    dairy_profile = Column(String())
   



    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'name: {self.name}, ' + \
            f'meat type: {self.meat_type}', + \
            f'veg type: {self.veg_type}', + \
            f'flavor profile: {self.flavor_profile}' + \
            f'spice profile: {self.starch_profile}' + \
            f'spice profile: {self.spice_profile}' + \
            f'dairy_profile: {self.dairy_profile}'
    
    

class Wine(Base):
    __tablename__  = 'wines'
    #__tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(),  primary_key=True)
    name = Column(String())
    grape_varietal = Column(String())
    region  = Column(String())

    wine_meal = relationship('WineMeals', backref=backref('wine'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'name: {self.name}, ' + \
            f'grape varietal: {self.grape_varietal}, ' + \
            f'region: {self.region}'
    


class WineMeals(Base):
    __tablename__  = 'wine_meal'
    #__tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(),  primary_key=True)
    meal_id = Column(Integer(), ForeignKey('meals.id'))
    wine_id = Column(Integer(), ForeignKey('wines.id'))

    def __repr__(self):
        return f'wine meal id: {self.id}, ' + \
            f'meal id: {self.meal_id}, ' + \
            f'region: {self.wine_id}'


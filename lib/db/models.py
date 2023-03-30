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
    starch_type = Column(String())
    spice_type = Column(String())
    dairy_type = Column(String())
   



    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'name: {self.name}, ' + \
            f'meat type: {self.meat_type}', + \
            f'veg type: {self.veg_type}', + \
            f'flavor profile: {self.flavor_profile}' + \
            f'spice profile: {self.starch_type}' + \
            f'spice profile: {self.spice_type}' + \
            f'dairy_profile: {self.dairy_type}'
    
    def __dir__(self):
        return [
            ('meat', self.meat_type), 
            ('veg', self.veg_type), 
            ('flavor', self.flavor_profile), 
            ('starch', self.starch_type), 
            ('spice', self.spice_type), 
            ('dairy', self.dairy_type)
        ]
        
    

class Wine(Base):
    __tablename__  = 'wines'
    #__tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(),  primary_key=True)
    name = Column(String())
    wine_type = Column(String())
    region  = Column(String())

    wine_meal = relationship('WineMeals', backref=backref('wine'))

    def __repr__(self):
        return f'id: {self.id}, ' + \
            f'name: {self.name}, ' + \
            f'wine type: {self.wine_type}, ' + \
            f'region: {self.region}'
    
    def __dir__(self):
        return [
            ('id', self.id),
            ('name', self.name),
            ('wine type', self.wine_type),
            ('region', self.region)
        ]


class WineMeals(Base):
    __tablename__  = 'wine_meal'
    #__tableargs__ = (PrimaryKeyConstraint('id'),)

    id = Column(Integer(),  primary_key=True)
    meal_id = Column(Integer(), ForeignKey('meals.id'))
    wine_id = Column(Integer(), ForeignKey('wines.id'))

    def __repr__(self):
        return f'wine meal id: {self.id}, ' + \
            f'meal id: {self.meal_id}, ' + \
            f'wine id: {self.wine_id}'


from ref_tables import *
from db.models import Base, Meal, Wine
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def add_new_meal(session):
    #clear_screen()
    print("You have decided to add a new meal.")
    name_input = input("Enter the new meal name: ")

    meat_type_input = input("Enter meat type (red meat, poultry, pork, fish, game, none): ")
    while (meat_type_input not in meat_list):
        meat_type_input = input("Enter valid meat type (red meat, poultry, pork, fish, game, none): ")

    veg_type_input = input("Enter primary veg type (allium, green leafy, root, nightshade, fungi, nuts or seeds, beans, none): ")
    while (veg_type_input not in veg_list):
        veg_type_input = input("Enter valid veg type (allium, green leafy, root, nightshade, fungi, nuts or seeds, beans, none): ")

    flavor_profile_input = input("Enter flavor profile (sweet, spicy, acidic, rich, bitter, salty): ")
    while (flavor_profile_input not in flavor_list):
        flavor_profile_input = input("Enter valid flavor profile (sweet, spicy, acidic, rich, bitter, salty): ")

    starch_input = input("Enter starch type (white, whole wheat, sweet veg, potato, none): ")
    while (starch_input not in starch_list):
        starch_input = input("Enter valid starch type (white, whole wheat, sweet veg, potato, none): ")

    spice_input = input("Enter main spice profile (black pepper, red pepper, hot and spicy, herbs, baking, other): ")
    while (spice_input not in spice_list):
        spice_input = input("Enter valid spice profile (black pepper, red pepper, hot and spicy, herbs, baking, other): ")

    dairy_input = input("Enter main dairy type (soft cheese or cream, hard cheese, pungent cheese, none): ")
    while (dairy_input not in dairy_list):
        spice_input = input("Enter valid dairy type (soft cheese or cream, hard cheese, pungent cheese, none): ")


    new_meal = Meal(name=name_input, meat_type=meat_type_input, veg_type=veg_type_input, flavor_profile=flavor_profile_input, starch_profile=starch_input, spice_profile=spice_input, dairy_profile=dairy_input)

    session.add(new_meal)
    session.commit()

    first_meal = session.query(Meal).first()
    print(first_meal.meat_type)

     #f'name: {self.name}, ' + \
            #f'meat type: {self.meat_type}', + \
            #f'veg type: {self.veg_type}', + \
            #f'flavor profile: {self.flavor_profile}' + \
            #f'spice profile: {self.starch_profile}' + \
            #f'spice profile: {self.spice_profile}' + \
            #f'dairy_profile: {self.dairy_profile}'
    


engine = create_engine('sqlite:///' + 'db/vino_geno.db', echo=True)
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#add_new_meal(session)

new_meal = Meal(name='roasted chicken', meat_type='poultry', veg_type='allium', flavor_profile='spicy', starch_profile='potato', spice_profile='black pepper', dairy_profile='none')

session.add(new_meal)
session.commit()
first_meal = session.query(Meal).first()
print(first_meal.name)


session.query(Meal).delete()

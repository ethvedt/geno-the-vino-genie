from ref_tables import *
from db.models import Base, Meal, Wine
import os

def add_new_meal(session):
    #clear_screen()
    print("You have decided to add a new meal.")
    name_input = input("Enter the new meal name: ")

    meat_type_input = input("Enter meat type (red meat, poultry, pork, fish, game, none): ")
    while (meat_type_input not in meat_list):
        meat_type_input = input("Enter valid meat type (red meat, poultry, pork, fish, game, none): ")

    veg_type_input = input("Enter primary veg type (allium, green leafy, root, nightshade, fungi, nuts or seeds, beans, none: ")
    while (veg_type_input not in veg_list):
        meat_type_input = input("Enter valid veg type (allium, green leafy, root, nightshade, fungi, nuts or seeds, beans, none: ")

    region_input = input("Enter region")


    #Meal(name=name_input, meat_type=meat_type_input, veg_type=veg_type_input, region, flavor_profile)

     #f'name: {self.name}, ' + \
            #f'meat type: {self.meat_type}', + \
            #f'veg type: {self.veg_type}', + \
            #f'flavor profile: {self.flavor_profile}' + \
            #f'spice profile: {self.starch_profile}' + \
            #f'spice profile: {self.spice_profile}' + \
            #f'dairy_profile: {self.dairy_profile}'
    


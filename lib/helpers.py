from ref_tables import *
from db.models import Base, Meal, Wine

def search_by_name(session):
    print("You have decided to search by name.")
    name_input = input("Type your meal here: ")
    meals = session.query(Meal).filter_by(Meal.name.contains(name_input)).all()


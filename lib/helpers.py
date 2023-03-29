from ref_tables import *
from db.models import Base, Meal, Wine, WineMeals
import os
from prettytable import PrettyTable
from recommenders import recommend_wine
from add_meal import add_new_meal

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main_page(session):
    clear_screen()
    print('''
   ______                          __   __             _    __ _                  ______              _     
  / ____/___   ____   ____        / /_ / /_   ___     | |  / /(_)____   ____     / ____/___   ____   (_)___ 
 / / __ / _ \ / __ \ / __ \      / __// __ \ / _ \    | | / // // __ \ / __ \   / / __ / _ \ / __ \ / // _ \\
/ /_/ //  __// / / // /_/ /_    / /_ / / / //  __/    | |/ // // / / // /_/ /  / /_/ //  __// / / // //  __/
\____/ \___//_/ /_/ \____/( )   \__//_/ /_/ \___/     |___//_//_/ /_/ \____/   \____/ \___//_/ /_//_/ \___/ 
                          |/                                                                                                                                                                
            ''')
    print('''
    ⠀⠀⠀⠀⠀⠀⣀⣀⣠⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⢿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⠿⠛⣁⣤⣤⣈⠛⠿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⣴⣶⣤⣈⠙⠻⠟⠋⣁⣤⣶⣦⣤⣀⠀⠀⠀⠀
⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀
⣾⣿⣿⣿⣿⣿⣧⣀⣀⣀⣀⣀⡀⠀⢀⣀⣠⣿⣿⣿⣿⣿⣿⣷
⠙⠿⣿⣿⣿⣿⣿⣿⠿⠿⠋⠁⠀⠶⢿⣿⣿⣿⣿⣿⣿⠿⠿⠋
⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣾⣿⣷⣶⣤⣤⣀⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠿⠟⠛⢉⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⣤⣶⣾⣿⣿⣿⣶⣶⣶⠶⠒⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠙⠛⠉⠉⠉⠀⠀⠀⠀
''')
    print("Hello! My name is Geno, and I will be your sommelier today. What would you like to do?")
    print('''
        1. Search for your meal by name.
        2. Search for your meal by parameters.
        3. Add a new meal to the database.
        4. Search the meal database.
        5. Search the wine database.
    ''')
    first_choice = input('Type the number of your choice: ')
    choice_table = {
        "1": search_by_name,
        "2": search_by_parameters,
        "3": add_new_meal,
        "4": search_meal_database,
        "5": search_wine_database
    }
    try:
        choice_table[str(first_choice)](session)
    except:
        raise Exception("Invalid input!")
    
def search_by_name(session):
    clear_screen()
    print("You have decided to search by name.")
    name_input = input("Type your meal here: ")
    meals = session.query(Meal).filter(Meal.name.contains(name_input)).all()
    if not meals:
        print("I'm sorry! Your meal is not in the database. Would you like to add it now?")
        yesno = input("y/n")
        if yesno == "y":
            return add_new_meal(session)
        elif yesno == "n":
            return main_page(session)
    elif len(meals) == 1:
        print(meals[0].__repr__())
    else:
        table = PrettyTable()
        table.field_names = [attr for attr in meals.__table__.columns]
        for meal in meals:
            table.add_row([value for attribute, value in dir(meal)])
        print(table)
    meal_choice = int(input("Is your meal present in the list? Select it by its ID now: "))
    selected_meal = next((meal for meal in meals if meal.id == meal_choice), None)
    if not selected_meal:
        raise ValueError("Please select a valid ID.")
    wine_list = recommend_wine(selected_meal, session)




        
def add_meal(session):
    add_new_meal(session)
    

def search_by_parameters(session):
    pass

def search_meal_database(session):
    pass

def search_wine_database(session):
    pass


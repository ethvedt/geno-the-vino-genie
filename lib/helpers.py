from ref_tables import *
from db.models import Base, Meal, Wine
import os

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
    ''')
    first_choice = input('Type the number of your choice: ')
    if first_choice == 1:
        search_by_name(session)
    elif first_choice == 2:
        search_by_parameters(session)
    elif first_choice == 3:
        add_new_meal(session)
    else:
        raise Exception("Invalid input!")
    
def search_by_name(session):
    clear_screen()
    print("You have decided to search by name.")
    name_input = input("Type your meal here: ")
    meals = session.query(Meal).filter_by(Meal.name.contains(name_input)).all()
    if not meals:
        print("I'm sorry! Your meal is not in the database. Would you like to add it now?")
        yesno = input("y/n")
        if yesno == "y":
            add_new_meal(session)
        elif yesno == "n":
            
            main_page(session)

def add_new_meal(session):
    pass

def search_by_parameters(session):
    pass

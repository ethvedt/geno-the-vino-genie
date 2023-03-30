from ref_tables import *
from db.models import Base, Meal, Wine, WineMeals
import os
from prettytable import PrettyTable
from recommenders import recommend_wine
import random
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
        1. Search for your meal by name.\n
        2. Search for your meal by parameters.\n
        3. Add a new meal to the database.\n
        6. Search the wine database.\n
    ''')
    choice_table = {
        "1": search_by_name,
        "2": search_by_parameters,
        "3": add_new_meal,
        "4": search_wine_database
    }
    first_choice = input('Type the number of your choice: ')
    try:
        choice_table[str(first_choice)](session)
    except:
        raise Exception("Invalid input!")
    
def search_by_name(session):
    clear_screen()
    print("You have decided to search by name.")
    name_input = input("Type your meal here: ")
    meals = session.query(Meal).filter(Meal.name.contains(name_input)).all()
    return refine_meal_search(meals, session)

def suggest_wine(wine_list, session, suggested_wines=[]):
    clear_screen()
    if set(wine_list) == set(suggested_wines):
        print("I'm sorry! We don't have any more wine to suggest to you. Returning to the main menu.")
        return main_page()
    wine_choice = random.choice(wine_list)
    while wine_choice in suggested_wines:
        wine_choice = random.choice(wine_list)
    suggested_wines.append(wine_choice)
    print(f'May I suggest a {wine_choice.name} for your meal?')
    ask_again = input("Would you like a different suggestion? y/n:")
    while ask_again not in ['y', 'n']:
        print("Please enter 'y' or 'n':")
        ask_again = input("Would you like a different suggestion? y/n: ")
    if ask_again == 'y':
        return suggest_wine(wine_list, session, suggested_wines)
    elif ask_again == 'n':
        return main_page(session)

def search_by_parameters(session):
    clear_screen()
    print("You have decided to search for your meal by its ingredients")
    meat_type_input = input("Enter meat type (red meat, poultry, pork, fish, game, none) or write 'pass' to skip: ")
    while (meat_type_input not in meat_list or meat_type_input != 'pass'):
        meat_type_input = input("Enter valid meat type (red meat, poultry, pork, fish, game, none) or write 'pass' to skip: ")
    print(meat_type_input)

    veg_type_input = input("Enter primary veg type (allium, green leafy, root, nightshade, fungi, nuts or seeds, beans, none) or write 'pass' to skip: ")
    while (veg_type_input not in veg_list or veg_type_input != 'pass'):
        veg_type_input = input("Enter valid veg type (allium, green leafy, root, nightshade, fungi, nuts or seeds, beans, none) or write 'pass' to skip: ")
    print(veg_type_input)

    flavor_profile_input = input("Enter flavor profile (sweet, spicy, acidic, rich, bitter, salty) or write 'pass' to skip: ")
    while (flavor_profile_input not in flavor_list or flavor_profile_input != 'pass'):
        flavor_profile_input = input("Enter valid flavor profile (sweet, spicy, acidic, rich, bitter, salty) or write 'pass' to skip: ")
    print(flavor_profile_input)

    starch_input = input("Enter starch type (white, whole wheat, sweet veg, potato, none) or write 'pass' to skip: ")
    while (starch_input not in starch_list or starch_input != 'pass'):
        starch_input = input("Enter valid starch type (white, whole wheat, sweet veg, potato, none) or write 'pass' to skip: ")
    print(starch_input)

    spice_input = input("Enter main spice profile (black pepper, red pepper, hot and spicy, herbs, baking, other) or write 'pass' to skip: ")
    while (spice_input not in spice_list or spice_input != 'pass'):
        spice_input = input("Enter valid spice profile (black pepper, red pepper, hot and spicy, herbs, baking, other) or write 'pass' to skip: ")
    print(spice_input)

    dairy_input = input("Enter main dairy type (soft cheese or cream, hard cheese, pungent cheese, none) or write 'pass' to skip: ")
    while (dairy_input not in dairy_list or dairy_input != 'pass'):
        spice_input = input("Enter valid dairy type (soft cheese or cream, hard cheese, pungent cheese, none) or write 'pass' to skip: ")
    print(dairy_input)

    inputs = {'meat_type': meat_type_input, 'veg_type': veg_type_input, 'flavor_profile': flavor_profile_input, 'starch_type': starch_input, 'spice_type': spice_input, 'dairy_type': dairy_input}

    if set(inputs.values()) == {'pass'}:
        print("Please select at least one filter for your search!")
        return search_by_parameters(session)
    meals = session.query(Meal).all()
    for key, value in inputs.items():
        if value == 'pass':
            pass
        else:
            meals.filter(getattr(Meal, key) == value)
    return refine_meal_search(session, meals)


def refine_meal_search(session, meals):
    if not meals:
        print("I'm sorry! Your meal is not in the database. Would you like to add it now?")
        yesno = input("y/n")
        while yesno not in ['y', 'n']:
            print("Please enter 'y' or 'n':")
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
    while not selected_meal:
        meal_choice = int(input("Is your meal present in the list? Select it by its ID now: "))
        selected_meal = next((meal for meal in meals if meal.id == meal_choice), None)
    wine_list = recommend_wine(selected_meal, session)
    return suggest_wine(wine_list, session)

def search_wine_database(session):
    clear_screen()
    print("You have decided to search the wine database. How would you like to search?")
    print('''
        1. Search by name.\n
        2. Search by wine type.\n
        3. Search by region.
    ''')
    select = input("Type the number of your selection here: ")
    while input not in [1, 2, 3]:
        print("Please select a valid number.")
        select = input("Type the number of your selection here: ")
    if input == 1:
        search = input("Please write the name of the wine here:")
        results = session.query(Wine).filter_by(Wine.name.contains(search)).all()
        make_wine_table(results)
    elif input == 2:
        search = input('Please write the name of the wine here ("bold red", "medium red", "light red", "rose", "rich white", "light white", "sparkling", "sweet white", "dessert"):')
        results = session.query(Wine).filter_by(Wine.wine_type.contains(search)).all()
        make_wine_table(results)
    elif input == 3:
        search = input("Type your desired region here:")
        results = session.query(Wine).filter_by(Wine.region.contains(search)).all()
        make_wine_table(results)
    yes_no = input("Would you like to search again? y/n: ")
    while yes_no not in ['y', 'n']:
        print("Please type 'y' or 'n'.")
        yes_no = input("Would you like to search again? y/n: ")
    if yes_no == 'y':
        return search_wine_database(session)
    elif yes_no == 'n':
        return main_page(session)

    
def make_wine_table(wine_list):
    t = PrettyTable()
    t.field_names = [attr for attr in Wine.__table__.columns]
    for wine in wine_list:
        t.add_row([value for attribute, value in dir(wine)])
    return print(t)
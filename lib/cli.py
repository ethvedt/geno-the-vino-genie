# from db.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///vino_geno.db')
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    print('''
   ______                          __   __             _    __ _                  ______              _     
  / ____/___   ____   ____        / /_ / /_   ___     | |  / /(_)____   ____     / ____/___   ____   (_)___ 
 / / __ / _ \ / __ \ / __ \      / __// __ \ / _ \    | | / // // __ \ / __ \   / / __ / _ \ / __ \ / // _ \\
/ /_/ //  __// / / // /_/ /_    / /_ / / / //  __/    | |/ // // / / // /_/ /  / /_/ //  __// / / // //  __/
\____/ \___//_/ /_/ \____/( )   \__//_/ /_/ \___/     |___//_//_/ /_/ \____/   \____/ \___//_/ /_//_/ \___/ 
                          |/                                                                                                                                                                
            ''')
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
        raise Exception("Invalid input")
    




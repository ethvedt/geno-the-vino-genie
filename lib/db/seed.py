from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Meal, Wine, WineMeals


bold_red_wines = [
    'Cabernet Sauvignon', 
    'Malbec', 
    'Syrah/Shiraz', 
    'Zinfandel', 
    'Merlot'
]

medium_red_wines = [
    'Pinot Noir', 
    'Barbera', 
    'Grenache/Garnacha', 
    'Sangiovese', 
    'Tempranillo'
]

light_red_wines = [
    'Gamay', 
    'Pinot Noir (Burgundy)', 
    'Counoise', 
    'Frappato', 
    'St. Laurent'
]

rose_wines = [
    'Provence Rosé', 
    'Tavel', 
    'Bandol Rosé', 
    'Côtes de Provence Rosé', 
    'Dry Rosé'
]

rich_white_wines = [
    'Chardonnay', 
    'Viognier', 
    'Marsanne', 
    'Roussanne', 
    'Semillon'
]

light_white_wines = [
    'Pinot Grigio', 
    'Sauvignon Blanc', 
    'Albariño', 
    'Vermentino', 
    'Gruner Veltliner'
]

sparkling_wines = [
    'Champagne', 
    'Prosecco', 
    'Cava', 
    'Crémant', 
    'California Sparkling Wine'
]

sweet_white_wines = [
    'Riesling (late harvest)', 
    "Moscato d'Asti", 
    'Ice Wine', 
    'Sauternes', 
    'Tokaji'
]

dessert_wines = [
    'Port', 
    'Sherry', 
    'Madeira', 
    'Vin Santo', 
    'Banyuls'
]

wines = {
    "bold red": bold_red_wines,
    "medium red": medium_red_wines,
    "light red": light_red_wines,
    "rose": rose_wines,
    "rich white": rich_white_wines,
    "light white": light_white_wines,
    "sparkling": sparkling_wines,
    "sweet white": sweet_white_wines,
    "dessert": dessert_wines
         }

bold_red_regions = [
    'Napa Valley, California', 
    'Tuscany, Italy', 
    'Mendoza, Argentina', 
    'Rhone Valley, France', 
    'Barossa Valley, Australia'
]

medium_red_regions = [
    'Rioja, Spain', 
    'Burgundy, France', 
    'Willamette Valley, Oregon', 
    'Central Otago, New Zealand', 
    'Veneto, Italy'
]

light_red_regions = [
    'Beaujolais, France', 
    'Mosel, Germany', 
    'Piedmont, Italy', 
    'Marlborough, New Zealand', 
    'Yarra Valley, Australia'
]

rose_wine_regions = [
    'Provence, France', 
    'Navarra, Spain', 
    'Central Coast, California', 
    'Tuscany, Italy', 
    'Languedoc-Roussillon, France'
]

rich_white_regions = [
    'Burgundy, France',
    'Napa Valley, California',
    'Mosel, Germany',
    'Friuli-Venezia Giulia, Italy',
    'Hunter Valley, Australia'
]

light_white_regions = [
    'Loire Valley, France', 
    'Mendoza, Argentina', 
    'Marlborough, New Zealand', 
    'Mosel, Germany', 
    'Rueda, Spain'
]

sparkling_wine_regions = [
    'Champagne, France',
    'Prosecco, Italy',
    'Cava, Spain',
    'Sekt, Germany',
    'California, USA'
]

sweet_white_regions = [
    'Sauternes, France',
    'Tokaji, Hungary',
    "Moscato d'Asti, Italy",
    'Rheingau, Germany',
    'Alsace, France'
]

dessert_wine_regions = [
    'Sauternes, Bordeaux, France', 
    'Porto, Douro Valley, Portugal', 
    'Tokaj, Hungary', 
    "Moscato d'Asti, Piedmont, Italy", 
    'Ice Wine, Ontario, Canada'
]



engine = create_engine('sqlite:///vino_geno.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Meal).delete()
session.query(Wine).delete()
session.query(WineMeals).delete()

faker = Faker()
meals = []
all_wines = []


def create_wines():
    import sys
    sys.path.append('..')
    from ref_tables import wine_list

    for wine_type in wine_list:
        for selection_name in wines[wine_type]:
            if (wine_type == "bold red"):
                for region in bold_red_regions:
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "medium red"):
                for region in medium_red_regions:
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)
                    
                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "light red"):
                for region in light_red_regions:
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "rose"):
                for region in rose_wine_regions: 
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "rich white"):
                for region in rich_white_regions: 
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "light white"):
                for region in light_white_regions: 
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)

            elif (wine_type == "sparkling"):
                for region in sparkling_wine_regions: 
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "sweet white"):
                for region in sweet_white_regions: 
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
            elif (wine_type == "dessert"):
                for region in dessert_wine_regions: 
                    wine_instance = Wine(name=selection_name, region=region,wine_type=wine_type)

                    session.add(wine_instance)
                    session.commit()

                    all_wines.append(wine_instance)
                

def create_meals():
    import sys
    sys.path.append('..')
    from ref_tables import meat_list, veg_list, flavor_list, starch_list, spice_list, dairy_list

    count = 1
    for _ in range(100):
        meal_name = 'meal' + str(count)
        meal = Meal(name=meal_name, meat_type=random.choice(meat_list), veg_type=random.choice(veg_list), flavor_profile=random.choice(flavor_list), starch_type=random.choice(starch_list), spice_type=random.choice(spice_list), dairy_type=random.choice(dairy_list))
        count += 1

        session.add(meal)
        session.commit()

        meals.append(meal)

    
    
    
    
def create_winemeals():
    import sys
    sys.path.append('..')
    import search

    for meal in meals:
        selected_wine_type = search.meal_search(meal)[0]

        selections = []

        wines = session.query(Wine).filter_by(wine_type = selected_wine_type).all()
        for wine in wines:
            wine_meal = WineMeals(meal_id=meal.id, wine_id=wine.id)
            session.add(wine_meal)
            session.commit()
            selections.append(wine)
            


create_wines()
create_meals()
create_winemeals()
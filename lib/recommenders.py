from db.models import Base, Meal, Wine, WineMeals
import random
from search import meal_search

def recommend_wine(meal, session):
    assoc = session.query(WineMeals).filter(WineMeals.meal_id == meal.id).all()
    results = []
    for entry in assoc:
        results.append(session.query(Wine).filter(Wine.id == entry.wine_id))
    if results:
        return results
    else:
        suggested_wine = meal_search(meal)[0]
        return select_wine_by_type(suggested_wine, session)

def select_wine_by_type(wine_type, session):
    results = session.query(Wine).filter(Wine.wine_type == wine_type).all()
    return results

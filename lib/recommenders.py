def recommend_wine(meal, session):
    assoc = session.query(WineMeals).filter(WineMeals.meal_id == meal.id).all()
    results = []
    for entry in assoc:
        results = session.query(Wine).filter(Wine.id == entry.wine_id)
    return results
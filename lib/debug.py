from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from add_meal import add_new_meal
from helpers import suggest_wine
from db.models import Meal, Wine
import random
from recommenders import recommend_wine


engine = create_engine('sqlite:///' + 'db/vino_geno.db')
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

random_wines = []
for _ in range(5):
    rand_wine = random.choice(session.query(Wine).all())
    random_wines.append(rand_wine)
   

meal = random.choice(session.query(Meal).all())
print(meal.vals())

results = recommend_wine(meal, session)

for result in results:
    print(result)
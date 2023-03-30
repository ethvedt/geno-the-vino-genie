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
    #print(rand_wine)

#suggest_wine(random_wines, session)


meal = random.choice(session.query(Meal).all())
print(dir(meal))

results = recommend_wine(meal, session)

for result in results:
    print(result)


#add_new_meal(session)

#new_meal = Meal(name='roasted chicken', meat_type='poultry', veg_type='allium', flavor_profile='spicy', starch_type='potato', spice_type='black pepper', dairy_type='none')

##session.add(new_meal)
#session.commit()
#meals = session.query(Meal).all()
#print([meal.name for meal in meals])


#session.query(Meal).delete()
#session.commit()

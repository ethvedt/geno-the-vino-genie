from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from add_meal import add_new_meal


engine = create_engine('sqlite:///' + 'db/vino_geno.db')
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

add_new_meal(session)

#new_meal = Meal(name='roasted chicken', meat_type='poultry', veg_type='allium', flavor_profile='spicy', starch_type='potato', spice_type='black pepper', dairy_type='none')

##session.add(new_meal)
#session.commit()
#meals = session.query(Meal).all()
#print([meal.name for meal in meals])


#session.query(Meal).delete()
#session.commit()

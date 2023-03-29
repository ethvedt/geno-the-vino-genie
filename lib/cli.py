# from db.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import main_page


engine = create_engine('sqlite:///' + 'db/vino_geno.db')
# Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    main_page(session)
    




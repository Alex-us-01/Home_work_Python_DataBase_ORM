import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

#DSN - data source name

DSN = 'postgresql://postgres:1793@localhost:5432/test'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()
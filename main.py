import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

#DSN - data source name

DSN = 'postgresql://postgres:1793@localhost:5432/test'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()

publisher_1 = Publisher(name='Publisher_1')
publisher_2 = Publisher(name='Publisher_2')
publisher_3 = Publisher(name='Publisher_3')
publisher_4 = Publisher(name='Publisher_4')

session.add_all([publisher_1, publisher_2, publisher_3, publisher_4])
session.commit()

# name_publisher = (input('Введите имя издателя:\n')).capitalize()


for c in session.query(Publisher).filter(Publisher.name == name_publisher).all():
    print(c)
session.commit()



session.close()
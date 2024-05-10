import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, search_publisher


DSN = 'postgresql://postgres:1793@localhost:5432/test'

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)

session = Session()
count = 1
list_publishers = []
for publisher in range(1000):
    name = Publisher(name='Publisher' + str(count))
    list_publishers.append(name)
    count += 1

session.add_all(list_publishers)

session.commit()


query_list = search_publisher()
column = query_list[0]
for c in session.query(Publisher).filter(column == query_list[1]).all():
    print(c)

session.commit()

session.close()

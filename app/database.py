from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.util import deprecations
from psycopg.rows import dict_row
import psycopg
import time
from app.config import settings

deprecations.SILENCE_UBER_WARNING = True

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Connecting to database using regular Postres driver(psycopg). Not used, connection made by SQLAlchemy
# while True:
        
#     try:
#         conn = psycopg.connect(dbname='FastApi Database', user='postgres', 
#                                password='Qwer1234$', row_factory=dict_row) # connect to db
#         cursor = conn.cursor()                         # open cursor to perform db operations
#         print('Database connectoin was succesfull!')
#         break
#     except Exception as error:
#         print('Connection to database failed')
#         print('Error:', error)
#         time.sleep(2)
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import pandas as pd

def create_database():
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:1234/postgres')
    session = scoped_session(sessionmaker(bind=engine))
    session.connection().connection.set_isolation_level(0)
    session.execute('CREATE DATABASE tes')
    session.close()

def create_schema():
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:1234/tes')
    session = scoped_session(sessionmaker(bind=engine))
    session.connection().connection.set_isolation_level(0)
    session.execute('CREATE SCHEMA IF NOT EXISTS retail')
    session.close()

def stage_table():
    engine = create_engine('postgresql+psycopg2://airflow:airflow@localhost:5432/airflow')
    session = scoped_session(sessionmaker(bind=engine))
    df = pd.read_sql('''SELECT * FROM retail.user_purchase''', engine)
    session.close()
    return df

def create_table():
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:1234/tes')
    session = scoped_session(sessionmaker(bind=engine))
    session.connection().connection.set_isolation_level(0)
    session.execute('''CREATE TABLE IF NOT EXISTS retail.user_purchase(
        invoice_number varchar(10),
        stock_code varchar(20),
        detail varchar(1000),
        quantity int,
        invoice_date timestamp,
        unit_price Numeric(8,3),
        customer_id int,
        country varchar(20)
     )''')
    session.close()

def insert_table(df):
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:1234/tes')
    session = scoped_session(sessionmaker(bind=engine))
    session.connection().connection.set_isolation_level(0)
    df.to_sql(name = 'user_purchase', schema = 'retail', con = engine,  if_exists='append', index=False)
    session.close()



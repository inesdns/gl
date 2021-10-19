import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.expression import insert
from etl_complete import drop_database, create_database, create_schema, stage_table, create_table, insert_table


def main():
    """
    Driver main function.
    """
    create_database()
    print("db created successfully!!")

    create_schema()
    print("schema created successfully!!")

    create_table()
    print("table created successfully!!")
    
    stage_table()

    df = stage_table()
    insert_table(df)
    print("table updated successfully!!")
    
if __name__ == "__main__":
    main()

main()

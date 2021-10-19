import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.expression import insert
from sqlalchemy.orm.session import close_all_sessions
from etl_final import main as etl_main


if __name__ == "__main__":
    etl_main()
    print("\n\nFinished updating data!\n\n")
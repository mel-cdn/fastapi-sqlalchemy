import os
from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PGSQLRepository(ABC):
    def __init__(self):
        self.session = sessionmaker(
            bind=create_engine(
                url="postgresql://{user}:{password}@{host}:{port}/{db_name}".format(
                    user=os.environ.get("POSTGRES_DB_USER"),
                    password=os.environ.get("POSTGRES_DB_PASSWORD"),
                    host=os.environ.get("POSTGRES_DB_HOST"),
                    port=os.environ.get("POSTGRES_DB_PORT"),
                    db_name=os.environ.get("POSTGRES_DB_NAME"),
                )
            ),
            autocommit=False,
            autoflush=False,
        )

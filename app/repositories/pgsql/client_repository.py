import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.database.pgsql.client import Client
from models.schema.client import ClientOut
from repositories.main_repository import MainRepository


class ClientRepository(MainRepository):
    def __init__(self):
        super().__init__()
        self.session = sessionmaker(
            bind=create_engine(os.environ.get("POSTGRES_DB_URL")),
            autocommit=False,
            autoflush=False,
        )
        self.model = Client

    def fetch(self) -> List[ClientOut]:
        print("Retrieving clients from PostgresSQL...")
        with self.session() as session:
            clients = session.query(Client).all()
        return [ClientOut(**client.camel_cased_dict()) for client in clients]

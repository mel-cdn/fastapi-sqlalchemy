from typing import List

from models.database.pgsql.client import Client
from models.schema.client import ClientOut
from repositories.main_repository import MainRepository
from repositories.pgsql.pgqsl_repository import PGSQLRepository


class ClientRepository(MainRepository, PGSQLRepository):
    def __init__(self):
        PGSQLRepository.__init__(self)
        self.model = Client

    def fetch(self) -> List[ClientOut]:
        print("Retrieving clients from PostgresSQL...")
        with self.session() as session:
            clients = session.query(Client).all()
        return [ClientOut(**client.camel_cased_dict) for client in clients]

    def create(self) -> ClientOut:
        print("Creating clients from PostgresSQL...")
        raise NotImplementedError

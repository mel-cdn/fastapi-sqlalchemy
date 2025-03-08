from typing import List

from models.schema.client import ClientOut
from repositories.main_repository import MainRepository


class ClientRepository(MainRepository):
    def __init__(self):
        super().__init__()
        print("Initialized DynamoDB ClientRepository...")

    def fetch(self) -> List[ClientOut]:
        print("Retrieving clients from DynamoDB...")
        raise NotImplementedError

    def create(self) -> ClientOut:
        """Mocked create. No actual data is being created."""
        print("Creating client in DynamoDB...")
        return ClientOut(**{"firstName": "Maximo", "lastName": "Dynamo Jr."})

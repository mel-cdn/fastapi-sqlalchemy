from typing import List

from models.schema.client import ClientOut
from repositories.main_repository import MainRepository


class ClientRepository(MainRepository):
    def __init__(self):
        super().__init__()
        print("Initialized DynamoDB ClientRepository...")

    def fetch(self) -> List[ClientOut]:
        """This is just to demonstrate dependency injection. No actual data is being fetched.
        ClientRepository of pgsql vs dynamodb.
        """
        print("Retrieving clients from DynamoDB...")
        return [ClientOut(**{"firstName": "John", "lastName": "Doe"})]

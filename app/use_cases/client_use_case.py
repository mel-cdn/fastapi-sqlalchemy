from typing import List

from models.schema.client import ClientOut
from repositories.main_repository import MainRepository


class ClientUseCase:
    def __init__(self, repo: MainRepository):
        self.repo = repo

    def fetch_entries(self) -> List[ClientOut]:
        print("Retrieving clients from whichever database...")
        clients = self.repo.fetch()
        print(f"Retrieved {len(clients)} client(s).")
        return clients

    def create_entry(self) -> ClientOut:
        print("Creating clients from whichever database...")
        client = self.repo.create()
        print(f"Created client: {client}")
        return client

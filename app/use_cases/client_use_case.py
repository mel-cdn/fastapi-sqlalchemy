import logging
from typing import List

from models.schema.client import ClientOut
from repositories.main_repository import MainRepository


class ClientUseCase:

    def __init__(self, repo: MainRepository):
        self.repo = repo

    def fetch_data(self) -> List[ClientOut]:
        print("Retrieving clients from whichever database...")
        clients = self.repo.fetch()
        print(f"Retrieved {len(clients)} client(s).")
        return clients

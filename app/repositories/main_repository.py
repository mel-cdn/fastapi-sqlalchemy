from abc import ABC, abstractmethod
from datetime import datetime


class MainRepository(ABC):
    """
    Abstract base class for main repositories.
    """

    def __init__(self):
        self.current_date = datetime.now().isoformat()

    @abstractmethod
    def fetch(self, **kwargs):
        """Retrieve data from the database."""

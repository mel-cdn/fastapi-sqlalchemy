from models.database.pgsql.core import CoreModel
from sqlalchemy.orm import Mapped, mapped_column


class Client(CoreModel):
    """Client Model"""
    
    __tablename__ = "Clients"

    Id: Mapped[int] = mapped_column(primary_key=True)
    FirstName: Mapped[str]
    LastName: Mapped[str]

    @property
    def camel_cased_dict(self) -> dict:
        return {
            "id": self.Id,
            "firstName": self.FirstName,
            "lastName": self.LastName,
            "age": 12,
        }

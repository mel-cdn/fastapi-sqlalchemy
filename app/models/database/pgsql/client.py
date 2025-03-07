from sqlalchemy.orm import Mapped, mapped_column

from models.database.pgsql.core import CoreModel


class Client(CoreModel):
    __tablename__ = "Clients"

    Id: Mapped[int] = mapped_column(primary_key=True)
    FirstName: Mapped[str]
    LastName: Mapped[str]


    def camel_cased_dict(self) -> dict:
        return {
            "id": self.Id,
            "firstName": self.FirstName,
            "lastName": self.LastName
        }

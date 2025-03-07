from pydantic import BaseModel, ConfigDict, Field


class ClientOut(BaseModel):
    model_config = ConfigDict(extra="ignore")

    firstName: str = Field(..., description="First name of the client")
    lastName: str = Field(..., description="Last name of the client")

from dependencies.client_dependencies import get_client_use_case
from fastapi import APIRouter
from fastapi.params import Depends
from models.schema.client import ClientOut
from use_cases.client_use_case import ClientUseCase

client_router = APIRouter()


@client_router.get(
    "",
    response_model=list[ClientOut],
    summary="Retrieve Clients",
    description="Retrieve all clients.",
)
async def retrieve_clients(client_use_case: ClientUseCase = Depends(get_client_use_case)):
    return client_use_case.fetch_entries()


@client_router.post(
    "",
    response_model=ClientOut,
    summary="Create Clients",
    description="Create new clients.",
)
async def create_client(client_use_case: ClientUseCase = Depends(get_client_use_case)):
    return client_use_case.create_entry()

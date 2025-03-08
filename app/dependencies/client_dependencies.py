from fastapi import Request
from repositories.dynamodb.client_repository import (
    ClientRepository as DynamoClientRepository,
)
from repositories.pgsql.client_repository import (
    ClientRepository as PostgresClientRepository,
)
from use_cases.client_use_case import ClientUseCase


def get_client_use_case(request: Request) -> ClientUseCase:
    if request.method == "GET" and request.url.path.split("/")[-1] == "clients/":
        # If GET /clients use PostgresSQL
        return ClientUseCase(repo=PostgresClientRepository())
    else:
        # e.g. POST /clients and other stuffs
        return ClientUseCase(repo=DynamoClientRepository())

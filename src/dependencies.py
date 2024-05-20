from typing import Annotated

from fastapi import Depends

from src.repositories.client import ClientRepository


class Dependencies:
    _client_repository: ClientRepository

    @classmethod
    def get_client_repository(cls) -> ClientRepository:
        return cls._client_repository

    @classmethod
    def set_client_repository(cls, client_repository: ClientRepository):
        cls._client_repository = client_repository


CLIENT_REPOSITORY_DEPENDENCY = Annotated[ClientRepository, Depends(Dependencies.get_client_repository)]

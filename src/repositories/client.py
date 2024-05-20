from fastapi import HTTPException

from src.exceptions import ClientNotFound
from src.schemas.client import FullClientSchema
from src.storage.abc import AbstractStorage


class ClientRepository:

    def __init__(self, storage: AbstractStorage):
        self.storage = storage

    async def create(self, client_data: FullClientSchema) -> FullClientSchema:
        return await self.storage.create(client_data)

    async def read(self, phone_number: str) -> str:
        address = await self.storage.read(phone_number)
        if address is None:
            raise ClientNotFound()
        return address

    async def update(self, client_data: FullClientSchema) -> FullClientSchema:
        return await self.storage.update(client_data)

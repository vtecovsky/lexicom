from fastapi import HTTPException
from redis.asyncio import Redis

from src.config import settings
from src.exceptions import ClientNotFound, ClientAlreadyExists
from src.schemas.client import FullClientSchema
from src.storage.abc import AbstractStorage


class RedisStorage(AbstractStorage):
    def __init__(self):
        self.redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

    async def initialize(self):
        await self.redis.initialize()

    async def close(self):
        await self.redis.close()

    async def create(self, client_model: FullClientSchema) -> FullClientSchema:
        res = await self.read(client_model.phone)
        if res is None:
            await self.redis.set(client_model.phone, client_model.address)
            return FullClientSchema(**client_model.model_dump())
        raise ClientAlreadyExists()

    async def update(self, client_model: FullClientSchema):
        res = await self.read(client_model.phone)
        if res is not None:
            await self.redis.set(client_model.phone, client_model.address)
            return FullClientSchema(**client_model.model_dump())
        raise ClientNotFound()

    async def read(self, phone_number: str) -> str | None:
        address = await self.redis.get(phone_number)
        if address:
            return address.decode('utf-8')

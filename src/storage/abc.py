from abc import ABC, abstractmethod

from src.schemas.client import FullClientSchema, PhoneSchema


class AbstractStorage(ABC):
    @abstractmethod
    async def create(self, client_model: FullClientSchema) -> FullClientSchema:
        raise NotImplementedError()

    @abstractmethod
    async def read(self, phone_number: str):
        raise NotImplementedError()

    @abstractmethod
    async def update(self, client_model: FullClientSchema):
        raise NotImplementedError()

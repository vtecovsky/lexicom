from typing import Annotated

from fastapi import Query

from src.api import router
from src.dependencies import CLIENT_REPOSITORY_DEPENDENCY
from src.schemas.client import FullClientSchema, AddressSchema


@router.get("/check_data", status_code=200)
async def check_data(client_repository: CLIENT_REPOSITORY_DEPENDENCY,
                     phone: Annotated[str | None, Query(pattern=r'^\+?\d{11}$')]) -> AddressSchema:
    address = await client_repository.read(phone_number=phone)
    return AddressSchema(address=address)


@router.post("/write_data", status_code=201)
async def write_data(client_data: FullClientSchema,
                     client_repository: CLIENT_REPOSITORY_DEPENDENCY) -> FullClientSchema:
    result = await client_repository.create(client_data=client_data)
    return FullClientSchema(**result.model_dump())


@router.put("/write_data", status_code=200)
async def write_data(client_data: FullClientSchema,
                     client_repository: CLIENT_REPOSITORY_DEPENDENCY) -> FullClientSchema:
    result = await client_repository.update(client_data=client_data)
    return FullClientSchema(**result.model_dump())

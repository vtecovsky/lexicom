from pydantic import BaseModel, Field


class FullClientSchema(BaseModel):
    phone: str = Field(pattern=r'^\+?\d{11}$', default='89090000000')
    address: str


class PhoneSchema(BaseModel):
    phone: str = Field(pattern=r'^\+?\d{11}$', default='89090000000')


class AddressSchema(BaseModel):
    address: str

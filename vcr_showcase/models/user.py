from pydantic import BaseModel, Field, TypeAdapter, ConfigDict
from pydantic.alias_generators import to_camel


class Coordinates(BaseModel):
    lat: float
    lng: float


class Address(BaseModel):
    address: str
    city: str
    state: str
    state_code: str
    postal_code: str
    coordinates: Coordinates
    country: str

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class Bank(BaseModel):
    card_expire: str
    card_number: str
    card_type: str
    currency: str
    iban: str

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class CompanyAddress(Address):
    pass


class Company(BaseModel):
    department: str
    name: str
    title: str
    address: CompanyAddress


class Hair(BaseModel):
    color: str
    type_: str = Field(alias="type")

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class Crypto(BaseModel):
    coin: str
    wallet: str
    network: str


class User(BaseModel):
    id_: int = Field(alias="id")
    first_name: str
    last_name: str
    maiden_name: str
    age: int
    gender: str
    email: str
    phone: str
    username: str
    password: str
    birth_date: str
    image: str
    blood_group: str
    height: float
    weight: float
    eye_color: str
    hair: Hair
    ip: str
    address: Address
    mac_address: str
    university: str
    bank: Bank
    company: Company
    ein: str
    ssn: str
    user_agent: str
    crypto: Crypto
    role: str

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )


class LoginInformation(BaseModel):
    username: str
    password: str


UserList = TypeAdapter(list[User])

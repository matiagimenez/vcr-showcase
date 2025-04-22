from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter


class User(BaseModel):
    id_: UUID = Field(alias="id")
    name: str
    email: str

    model_config = ConfigDict(populate_by_name=True)


UserValidator = TypeAdapter(list[User])

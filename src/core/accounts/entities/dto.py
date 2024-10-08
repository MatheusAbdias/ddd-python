from pydantic import BaseModel

from src.core.accounts.entities.enums import AccountType


class AccountReadDTO(BaseModel):
    id: int
    type: AccountType
    balance: int

    class Config:
        from_attributes = True


class AccountRegistryDTO(BaseModel):
    name: str
    type: AccountType

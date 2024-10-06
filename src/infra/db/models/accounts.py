import enum

from sqlmodel import Field

from src.infra.db.models.base import TimeStampedModel


class AccountType(str, enum.Enum):
    PERSONAL = "PERSONAL"
    BUSINESS = "BUSINESS"


class Account(TimeStampedModel, table=True):
    type: AccountType = Field(nullable=False)
    balance: int = Field(default=0, nullable=False)
    branch: str
    number: str

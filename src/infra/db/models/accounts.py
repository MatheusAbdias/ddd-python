from sqlmodel import Field

from core.accounts.entities.enums import AccountType
from infra.db.models.base import TimeStampedModel


class Account(TimeStampedModel):
    type: AccountType = Field(nullable=False)
    balance: int = Field(default=0, nullable=False)
    branch: str = Field(default="", nullable=False)
    number: str = Field(default="", nullable=False)

    def __repr__(self) -> str:
        return f"Account(id={self.id}, type={self.type}, balance={self.balance}"

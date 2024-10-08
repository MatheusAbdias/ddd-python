from sqlmodel import Field, Relationship

from src.core.accounts.entities.enums import AccountType
from src.infra.db.models.base import Model, TimeStampedModel
from src.infra.db.models.users import User


class Account(TimeStampedModel, table=True):
    type: AccountType = Field(nullable=False)
    balance: int = Field(default=0, nullable=False)
    branch: str = Field(default="", nullable=False)
    number: str = Field(default="", nullable=False)

    def __repr__(self) -> str:
        return f"Account(id={self.id}, type={self.type}, balance={self.balance}"


class AccountHolder(Model, table=True):
    user_id: int = Field(nullable=False, foreign_key="user.id", unique=True)
    account_id: int = Field(nullable=False, foreign_key="account.id", unique=True)

    user: User = Relationship(
        back_populates="account",
        link_model=User,
        sa_relationship_kwargs={"uselist": False},
    )
    account: Account = Relationship(
        back_populates="holder",
        link_model=Account,
        sa_relationship_kwargs={"uselist": False},
    )

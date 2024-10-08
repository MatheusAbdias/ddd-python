from datetime import datetime

from sqlmodel import Column, DateTime, Field, SQLModel, func


class Model(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class TimeStampedModel(Model):
    created_at: datetime = Field(
        default=func.now(),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
    )
    updated_at: datetime = Field(
        default=func.now(),
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )

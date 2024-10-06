from sqlmodel import Field, SQLModel


class Model(SQLModel):
    id: int | None = Field(default=None, primary_key=True)

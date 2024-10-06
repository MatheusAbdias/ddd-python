from src.infra.db.models.base import Model


class User(Model, table=True):
    first_name: str
    last_name: str
    age: int

    def __repr__(self):
        return f"Users [id={self.id}, first_name={self.first_name}]"

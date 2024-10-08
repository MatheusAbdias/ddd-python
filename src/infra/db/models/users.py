from src.infra.db.models.base import Model


class User(Model, table=True):
    document: str
    name: str

    def __repr__(self):
        return f"Users [id={self.id}, first_name={self.name}]"

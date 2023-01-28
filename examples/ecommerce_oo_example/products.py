import examples.ecommerce_oo_example.database as database

from .database import Database

from .database import Database as DB

from .database import Database, Query

from .contact.email import send_mail


class Product:
    def __init__(self, name: str) -> None:
        self.name = name

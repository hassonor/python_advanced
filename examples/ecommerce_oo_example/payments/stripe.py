from __future__ import annotations
from typing import Any

from ..database import Database
from ..contact.email import send_mail


def payment() -> dict[str, Any]:
    db = Database("path/to/data")
    return db.fetch("test_2")

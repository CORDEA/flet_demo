from dataclasses import dataclass


@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    tags: list[str]

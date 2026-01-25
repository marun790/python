from dataclasses import dataclass


@dataclass
class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

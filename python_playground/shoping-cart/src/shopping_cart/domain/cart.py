from dataclasses import dataclass
from shopping_cart.domain.product import Product


@dataclass
class Cart:

    cart_products: dict[Product, int]

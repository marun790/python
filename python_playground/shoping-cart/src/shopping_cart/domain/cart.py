from dataclasses import dataclass
from shopping_cart.domain.product import Product


@dataclass
class Cart:

    cart_products: dict[Product, int]

    def is_product_in_cart(self, product: Product) -> bool:
        return product in self.cart_products.keys()

    def increase_product_quantity(self, product: Product, quantity: int):
        self.cart_products[product] += quantity

    def add_product_to_cart(self, product: Product, quantity: int):
        self.cart_products[product] = quantity

    def delete_product_from_cart(self, product: Product) -> Product | None:
        if self.is_product_in_cart(product):
            deleted_product = self.cart_products.pop(product)
            print(f"Product {deleted_product} deleted from cart")
            return deleted_product
        return None

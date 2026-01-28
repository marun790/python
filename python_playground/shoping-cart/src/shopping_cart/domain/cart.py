from dataclasses import dataclass
from shopping_cart.domain.product import Product


@dataclass
class Cart:

    cart_products: dict[Product, int]

    def isProductInCart(self, product: Product) -> bool:
        return product in self.cart_products.keys()

    def increaseProductQuantity(self, product: Product, quantity: int):
        self.cart_products[product] += quantity

    def addProductToCart(self, product: Product, quantity: int):
        self.cart_products[product] = quantity

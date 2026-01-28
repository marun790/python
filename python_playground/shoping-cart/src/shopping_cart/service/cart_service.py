
from shopping_cart.domain.cart import Cart
from shopping_cart.domain.product import Product


class CartService:

    _user_cart: dict[str, Cart] = {}

    def add_product_to_cart(self, user: str, product: Product, quantity: int):
        if user not in self._user_cart.keys():
            self._user_cart[user] = Cart(cart_products={product: quantity})
        else:
            self._user_cart[user].cart_products[product] = quantity
        return self._user_cart[user]

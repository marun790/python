
from shopping_cart.domain.cart import Cart
from shopping_cart.domain.product import Product


class CartService:

    _user_cart: dict[str, Cart] = {}

    def add_product_to_cart(self, user: str, product: Product, quantity: int) -> Cart:

        cart = self.get_cart(user)
        if cart is None:
            # User adding the product to the cart for the first time
            cart = Cart(cart_products={product: quantity})
            self._user_cart[user] = cart
        elif cart.is_product_in_cart(product):
            # User adding the same product to the cart
            cart.increase_product_quantity(product, quantity)
        else:
            # User adding a new product to the cart
            cart.add_product_to_cart(product, quantity)
        return cart

    def get_cart(self, user: str) -> Cart | None:
        return self._user_cart.get(user, None)

    def delete_product_from_cart(self, user: str, product: Product) -> Cart | None:
        cart = self.get_cart(user)
        if cart is not None:
            cart.delete_product_from_cart(product)
        return cart

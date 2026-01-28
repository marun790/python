
from shopping_cart.domain.cart import Cart
from shopping_cart.domain.product import Product


class CartService:

    _user_cart: dict[str, Cart] = {}

    def add_product_to_cart(self, user: str, product: Product, quantity: int) -> Cart:

        cart = self.get_user_cart(user)
        if cart is None:
            # User adding the product to the cart for the first time
            cart = Cart(cart_products={product: quantity})
            self._user_cart[user] = cart
        elif cart.isProductInCart(product):
            # User adding the same product to the cart
            cart.increaseProductQuantity(product, quantity)
        else:
            # User adding a new product to the cart
            cart.addProductToCart(product, quantity)
        return cart

    def get_user_cart(self, user: str) -> Cart | None:
        return self._user_cart.get(user, None)

from shopping_cart.domain.cart import Cart
from shopping_cart.domain.product import Product
from shopping_cart.service.cart_service import CartService


class TestCartService:

    cart_service = CartService()

    def test_add_cart(self):
        product = Product(name="Test Product", price=100.00)
        user_cart = self.cart_service.add_product_to_cart(
            user="Test User", product=product, quantity=1)
        assert user_cart.cart_products == {product: 1}

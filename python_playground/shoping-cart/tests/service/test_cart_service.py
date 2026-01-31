
from shopping_cart.domain.product import Product
from shopping_cart.service.cart_service import CartService


class TestCartService:

    cart_service = CartService()

    def test_add_cart(self):
        product = Product(name="Test Product", price=100.00)
        cart = self.cart_service.add_product_to_cart(
            user="Test User", product=product, quantity=1)
        assert cart.cart_products == {product: 1}

    def test_add_same_product_to_cart_should_increase_the_quandity(self):
        product = Product(name="Test Product", price=100.00)
        self.cart_service.add_product_to_cart(
            user="Test User", product=product, quantity=1)
        cart = self.cart_service.add_product_to_cart(
            user="Test User", product=product, quantity=2)
        assert cart.cart_products == {product: 3}

    def test_adding_multiple_products_to_cart_should_add_the_products_to_the_cart(self):
        product1 = Product(name="Test Product 1", price=100.00)
        product2 = Product(name="Test Product 2", price=200.00)
        self.cart_service.add_product_to_cart(
            user="Test User", product=product1, quantity=2)
        self.cart_service.add_product_to_cart(
            user="Test User", product=product2, quantity=3)
        self.cart_service.add_product_to_cart(
            user="Test User", product=product1, quantity=2)

        final_user_cart = self.cart_service.get_cart(user="Test User")
        assert final_user_cart.cart_products == {product1: 4, product2: 3}

    def test_delete_product_from_cart(self):
        product = Product(name="Test Product", price=100.00)
        self.cart_service.add_product_to_cart(
            user="Test User", product=product, quantity=1)

        self.cart_service.delete_product_from_cart(
            user="Test User", product=product)
        print(
            f"Cart post delition {self.cart_service.get_cart(user='Test User').cart_products}")
        assert self.cart_service.get_cart(
            user="Test User").cart_products == {}



from shopping_cart.domain.product import Product


class TestProduct:

    def test_product_creation(self):
        product = Product(name="Test Product", price=100.00)
        assert product.name == "Test Product"
        assert product.price == 100.00

"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity

        tested_quantity = product.quantity
        assert product.check_quantity(tested_quantity), \
            f"It is not enough {tested_quantity} products of total {product.quantity}"
        tested_quantity = product.quantity - 1
        assert product.check_quantity(tested_quantity), \
            f"It is not enough {tested_quantity} products of total {product.quantity}"
        tested_quantity = product.quantity + 1
        assert not product.check_quantity(tested_quantity), \
            f"There is no {tested_quantity} products then total {product.quantity}"
        pass

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        tested_quantity = product.quantity - 1
        try:
            product.buy(tested_quantity)
        except ValueError:
            raise AssertionError(f"You couldn't buy {tested_quantity} products of total {product.quantity}")

    def test_product_buy_all(self, product):
        # TODO напишите проверки на метод buy
        tested_quantity = product.quantity
        try:
            product.buy(tested_quantity)
        except ValueError:
            raise AssertionError(f"You couldn't buy {tested_quantity} products of total {product.quantity}")

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        tested_quantity = product.quantity + 1
        try:
            product.buy(tested_quantity)
            raise AssertionError(f"You couldn't buy {tested_quantity} products of total {product.quantity}")
        except ValueError:
            assert True


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

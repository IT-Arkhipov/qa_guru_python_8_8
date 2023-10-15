"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()

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
        tested_quantity = product.quantity
        with pytest.raises(ValueError):
            product.buy(tested_quantity)
            assert False, f"You can't buy {tested_quantity} then it is"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        # Через переменную added_quant возможно проверить добавление любого количества товара
        # проверка добавления 1 товара
        added_quant = 1
        prev_quant = cart.products.get(product, 0)
        cart.add_product(product=product, buy_count=added_quant)
        new_quant = cart.products.get(product, 0)
        assert new_quant - prev_quant == added_quant, \
            f"To the cart added {new_quant - prev_quant} product then supposed {added_quant}"

    def test_add_product_zero(self, product, cart):
        # Через переменную added_quant возможно проверить добавление любого количества товара
        # проверка добавления 0 количества товаров
        added_quant = 0
        prev_quant = cart.products.get(product, 0)
        cart.add_product(product=product, buy_count=added_quant)
        new_quant = cart.products.get(product, 0)
        assert new_quant - prev_quant == added_quant, \
            f"To the cart added {new_quant - prev_quant} product then supposed {added_quant}"

    def test_add_product_negative(self, product, cart):
        # Через переменную added_quant возможно проверить добавление любого количества товара
        # проверка добавления отрицательного количества товаров
        added_quant = -1
        prev_quant = cart.products.get(product, 0)
        cart.add_product(product=product, buy_count=added_quant)
        new_quant = cart.products.get(product, 0)
        assert new_quant == prev_quant, f"There were added {added_quant} products to the cart"

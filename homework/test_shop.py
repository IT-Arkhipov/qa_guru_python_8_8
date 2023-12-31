"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def two_products():
    return (Product("book", 45.8, "This is a book", 86),
            Product("pen", 9.23, "This is a pen", 32))


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
        # Проверка граничных значений количества товара
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
        # граничное значение - 1
        tested_quantity = product.quantity - 1
        try:
            product.buy(tested_quantity)
        except ValueError:
            raise AssertionError(f"You couldn't buy {tested_quantity} products of total {product.quantity}")

    def test_product_buy_all(self, product):
        # TODO напишите проверки на метод buy
        # граничное значение
        tested_quantity = product.quantity
        try:
            product.buy(tested_quantity)
        except ValueError:
            raise AssertionError(f"You couldn't buy {tested_quantity} products of total {product.quantity}")

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        # граничное значение + 1
        tested_quantity = product.quantity + 1
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
            f"To the cart added {new_quant - prev_quant} product(s) then supposed {added_quant}"

    def test_add_product_zero(self, product, cart):
        # Через переменную added_quant возможно проверить добавление любого количества товара
        # проверка добавления 0 количества товаров
        added_quant = 0
        prev_quant = cart.products.get(product, 0)
        cart.add_product(product=product, buy_count=added_quant)
        new_quant = cart.products.get(product, 0)
        assert new_quant - prev_quant == added_quant, \
            f"To the cart added {new_quant - prev_quant} product(s) then supposed {added_quant}"

    def test_add_product_negative(self, product, cart):
        # Через переменную added_quant возможно проверить добавление любого количества товара
        # проверка добавления отрицательного количества товаров. Возможно тест не нужен, если отрицательные числа
        # отсекаются фронтом
        added_quant = -1
        prev_quant = cart.products.get(product, 0)
        cart.add_product(product=product, buy_count=added_quant)
        new_quant = cart.products.get(product, 0)
        assert new_quant == prev_quant, f"There were added {added_quant} product(s) to the cart"

    def test_remove_product(self, product, cart):
        # Добавляем определенное количество товара, удаляем половину (целую часть)
        # учитывается возможное предыдущее количество товара в корзине
        prev_quant = cart.products.get(product, 0)
        added_quant = 7
        cart.add_product(product=product, buy_count=added_quant)
        removed_quant = added_quant // 2
        cart.remove_product(product=product, remove_count=removed_quant)
        left_quant = cart.products.get(product, 0)
        assert prev_quant + added_quant - removed_quant == left_quant, f"Wrong {left_quant} product(s) left in the cart"

    def test_remove_product_all(self, product, cart):
        # Удаление всего количество товара, учитывается возможное предыдущее количество товара в корзине
        prev_quant = cart.products.get(product, 0)
        added_quant = 17
        cart.add_product(product=product, buy_count=added_quant)
        removed_quant = added_quant + prev_quant
        cart.remove_product(product=product, remove_count=removed_quant)
        left_quant = cart.products.get(product, 0)
        assert prev_quant + added_quant - removed_quant == left_quant, f"Wrong {left_quant} product(s) left in the cart"

    def test_remove_product_more_than(self, product, cart):
        # Удаление количество товара, больше чем в корзине. Учитывается возможное предыдущее количество товара в корзине
        prev_quant = cart.products.get(product, 0)
        added_quant = 21
        cart.add_product(product=product, buy_count=added_quant)
        removed_quant = added_quant + prev_quant + 1
        cart.remove_product(product=product, remove_count=removed_quant)
        left_quant = cart.products.get(product, 0)
        assert left_quant == 0, "No products supposed to be left in the cart"

    def test_remove_product_complete(self, product, cart):
        # Удаление всего количество товара, если не передано количество - remove_count=None
        added_quant = 99
        cart.add_product(product=product, buy_count=added_quant)
        cart.remove_product(product=product, remove_count=None)
        left_quant = cart.products.get(product, 0)
        assert left_quant == 0, "No products supposed to be left in the cart"

    def test_remove_product_more_negative(self, product, cart):
        # Удаление отрицательного количество товара - удаление не происходит
        prev_quant = cart.products.get(product, 0)
        added_quant = 42
        cart.add_product(product=product, buy_count=added_quant)
        removed_quant = -7
        cart.remove_product(product=product, remove_count=removed_quant)
        left_quant = cart.products.get(product, 0)
        assert prev_quant + added_quant == left_quant, "No products supposed to be removed from the cart"

    def test_clear_cart(self, cart, two_products):
        # Добавляем 2 продукта в корзину, затем очищаем всю корзину
        product1, product2 = two_products

        quantity1 = 16
        quantity2 = 25
        cart.add_product(product=product1, buy_count=quantity1)
        cart.add_product(product=product2, buy_count=quantity2)

        cart.clear()
        assert cart.products == {}, "The cleared cart is not empty"

    def test_total_price(self, cart, two_products):
        # Добавляем 2 продукта в корзину, затем получаем стоимость корзины
        product1, product2 = two_products

        quantity1 = 31
        quantity2 = 17
        cart.add_product(product=product1, buy_count=quantity1)
        cart.add_product(product=product2, buy_count=quantity2)

        total_price = product1.price * quantity1 + product2.price * quantity2
        cart_total_price = cart.get_total_price()
        assert cart_total_price == total_price, (f"The cart total price {cart_total_price} "
                                                 f"doesn't equal products total price {total_price}")

    def test_buy(self, product, cart):
        # Добавляем товара в корзину меньше, чем количество на складе, с учетом предыдущего количества в корзине
        prod_quant = product.quantity
        prev_quant = cart.products.get(product, 0)
        added_quant = (prod_quant - prev_quant) // 2
        cart.add_product(product=product, buy_count=added_quant)
        try:
            cart.buy()
        except ValueError:
            raise AssertionError(f"An attempt to buy {added_quant + prev_quant} than {prod_quant} product(s)")
        else:
            assert product.quantity == prod_quant - added_quant - prev_quant, f"Not all product was bought"

    def test_buy_less_than(self, product, cart):
        # Добавляем товара в корзину на 1 товар меньше, чем на складе, с учетом предыдущего количества в корзине
        prod_quant = product.quantity
        prev_quant = cart.products.get(product, 0)
        added_quant = prod_quant - prev_quant - 1
        cart.add_product(product=product, buy_count=added_quant)
        try:
            cart.buy()
        except ValueError:
            raise AssertionError(f"An attempt to buy {added_quant + prev_quant} than {prod_quant} product(s)")
        else:
            assert product.quantity == 1, f"There are left {product.quantity} - more than 1 product"

    def test_buy_all(self, product, cart):
        # Добавляем товара весь товар, с учетом предыдущего количества в корзине
        # Проверяем, что весь товар был выкуплен
        prod_quant = product.quantity
        prev_quant = cart.products.get(product, 0)
        added_quant = prod_quant - prev_quant
        cart.add_product(product=product, buy_count=added_quant)
        try:
            cart.buy()
        except ValueError:
            raise AssertionError(f"An attempt to buy {added_quant + prev_quant} than {prod_quant} product(s)")
        else:
            assert product.quantity == 0, f"Not all product was bought"

    def test_buy_more_than(self, product, cart):
        prod_quant = product.quantity
        prev_quant = cart.products.get(product, 0)
        added_quant = (prod_quant - prev_quant) + 1
        cart.add_product(product=product, buy_count=added_quant)
        try:
            cart.buy()
        except ValueError:
            assert True
        else:
            raise AssertionError(f"An attempt to buy {added_quant + prev_quant} than {prod_quant} product(s)")
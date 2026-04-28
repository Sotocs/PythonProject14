import pytest

from scr.product import Product
from scr.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture()
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def product4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


def test_category1(product1, product2, product3):
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert category1.name == "Смартфоны"
    assert "Смартфоны" in category1.description
    assert category1.len_products == 3

    # Проверяем счётчики
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category2(product4):
    category2 = Category(
        "Телевизоры",
        "Современный телевизор",
        [product4],
    )

    assert category2.name == "Телевизоры"
    assert category2.len_products == 1

    # Проверка счётчиков
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product(product1):
    category = Category("Test", "Desc", [])

    category.add_product(product1)

    assert category.len_products == 1


def test_add_product_updates_list(product1):
    category = Category("Test", "Desc", [])

    category.add_product(product1)

    # Проверяем, что объект реально внутри
    assert category._Category__products[0] == product1


def test_products_output(product1, capsys):
    category = Category("Test", "Desc", [product1])

    category.products  # вызываем property

    captured = capsys.readouterr()
    assert product1.name in captured.out
    assert "руб." in captured.out


def test_len_products_empty():
    category = Category("Empty", "No products", [])
    assert category.len_products == 0

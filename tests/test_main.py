import pytest

from scr.main import Product, Category


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


def test_product(product1, product2, product3):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product2.name == "Iphone 15"
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product1.price == 180000.0
    assert product2.price == 210000.0
    assert product3.price == 31000.0
    assert product1.quantity == 5
    assert product2.quantity == 8
    assert product3.quantity == 14


def test_category1(product1, product2, product3):
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 3
    assert category1.products == [product1, product2, product3]
    assert category1.category_count == 1
    assert category1.product_count == 3


@pytest.fixture()
def product4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


def test_category2(product4):
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )
    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category2.products) == 1
    assert category2.products == [product4]


# def test_count(product4):
#     assert Category.category_count == 2
#     assert Category.product_count == 0

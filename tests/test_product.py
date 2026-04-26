import pytest

from scr.product import Product


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


@pytest.fixture()
def product4():
    return Product.new_product({'name':'55" QLED 4K', 'description':"Фоновая подсветка", 'price':123000.0, 'quantity':7})


def test_product2(product4):
    assert product4.name == '55" QLED 4K'
    assert product4.price == 123000.0
    assert product4.quantity == 7
    assert product4.description == "Фоновая подсветка"
    product4.price = 180000.0
    assert product4.price == 180000.0
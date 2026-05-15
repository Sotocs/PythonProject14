import pytest

from src.product import LawnGrass, Product, Smartphone

from src.product import BaseProduct


def test_base_product_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct()


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
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert product1 + product2 == 2580000


def test_zero_quantity():
    with pytest.raises(ValueError):
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0)


@pytest.fixture()
def product4():
    return Product.new_product(
        {
            "name": '55" QLED 4K',
            "description": "Фоновая подсветка",
            "price": 123000.0,
            "quantity": 7,
        }
    )


def test_product2(product4):
    assert product4.name == '55" QLED 4K'
    assert product4.price == 123000.0
    assert product4.quantity == 7
    assert product4.description == "Фоновая подсветка"
    product4.price = 180000.0
    assert product4.price == 180000.0


def test_price_increase(product1):
    product1.price = 200000.0
    assert product1.price == 200000.0


def test_price_decrease_reject(product1, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "n")

    old_price = product1.price
    product1.price = 100000.0

    assert product1.price == old_price


def test_price_zero(product1, capsys):
    old_price = product1.price

    product1.price = 0

    captured = capsys.readouterr()
    assert "не должна быть" in captured.out
    assert product1.price == old_price


def test_price_negative(product1, capsys):
    old_price = product1.price

    product1.price = -100

    captured = capsys.readouterr()
    assert "не должна быть" in captured.out
    assert product1.price == old_price


# tests for subclasses


@pytest.fixture()
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


def test_smartphone1(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


@pytest.fixture()
def grass1():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


def test_grass1(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_add_products(smartphone1, grass1):
    assert smartphone1 + smartphone1 == 1800000

    with pytest.raises(TypeError):
        smartphone1 + grass1

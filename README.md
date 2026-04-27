# Проект: Product & Category

## 📌 Описание

В проекте реализованы классы для работы с товарами и категориями.

* **Product** — описывает товар
* **Category** — описывает категорию товаров

Проект демонстрирует работу с:

* классами и объектами
* инкапсуляцией (`private` атрибуты)
* свойствами (`@property`)
* методами класса (`@classmethod`)

---

## ⚙️ Функциональность

### 🛍️ Класс Product

* хранит информацию о товаре:

  * название
  * описание
  * цена
  * количество
* реализован приватный атрибут цены (`__price`)
* добавлен getter и setter для цены:

  * запрещает устанавливать цену ≤ 0
  * запрашивает подтверждение при понижении цены
* реализован метод создания объекта из словаря:

  * `new_product()`

---

### 📦 Класс Category

* хранит:

  * название
  * описание
  * список товаров
* ведёт подсчёт:

  * количества категорий (`category_count`)
  * количества товаров (`product_count`)
* реализованы:

  * вывод списка товаров
  * добавление нового товара (`add_product`)
  * получение количества товаров (`len_products`)

---

## 🗂️ Структура проекта

```
project_root/
│
├── src/
│   ├── product.py
│   ├── category.py
│
├── tests/
│   ├── test_product.py
│   ├── test_category.py
│
├── data/
│   └── products.json
│
├── main.py
├── pyproject.toml
├── poetry.lock
├── README.md
```

---

## 🚀 Запуск проекта

```bash
python main.py
```

---

## 🧪 Тестирование

```bash
pytest
```

---

## 💡 Пример использования

```python
from scr.product import Product
from scr.category import Category

product = Product("Iphone 15", "512GB", 210000.0, 8)

category = Category("Смартфоны", "Описание", [product])
category.add_product(Product("Samsung", "Описание", 100000, 5))
```



## 📚 Используемые технологии

* Python 3
* Poetry
* Pytest

---

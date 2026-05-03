from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        for product in self.__products:
            print(product)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def len_products(self):
        return len(self.__products)

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError

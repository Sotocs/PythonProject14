


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
        for each_product in self.__products:
            print(f'{each_product.name}, {each_product.price} руб. Остаток: {each_product.quantity} шт.')

    @property
    def len_products(self):
        return len(self.__products)

    def add_product(self, product):
        self.__products.append(product)



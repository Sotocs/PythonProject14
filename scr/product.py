class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        return cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        result = self.price * self.quantity + other.price * other.quantity
        return result

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0:
            if price < self.__price:
                print("Цена понижается, подтвердите понижение y/n")
                answer = input()
                if answer == "y":
                    self.__price = price
            elif price > self.__price:
                self.__price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")

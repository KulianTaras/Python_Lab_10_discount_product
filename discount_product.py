class DiscountProduct:

    storage_product_number = 0

    def __init__(self, name="No name", discount=0.0, initial_price=0.0,
                 weight=0.0, manufacture_country="No name",
                 is_fragile=False):
        self._name = name
        self._discount = discount
        self._initial_price = initial_price
        self._discount_price = initial_price*discount/100
        self._weight = weight
        self._manufacture_country = manufacture_country
        self._is_fragile = is_fragile
        DiscountProduct.product_number()

    def __del__(self):
        print("Destroy", self._name)

    def __str__(self):
        return "Name: " + self._name + "\n Discount: " + str(self._discount) +\
               " %" + "\n Initial Price: " + str(self._initial_price) + " $" +\
               "\n Discount Price: " + str(self._discount_price) + " $" +\
               "\n Weight: " + str(self._weight) + " KG" + "\n Made in: " +\
               self._manufacture_country + "\n Is the product fragile: " + str(self._is_fragile)

    @staticmethod
    def product_number():
        DiscountProduct.storage_product_number += 1


def main():
    milk = DiscountProduct("Milk", 12.5, 50, 34, "Ukraine", True)
    bread = DiscountProduct("Bread", 5.55555, 24, 1.2, "German")
    ice_cream = DiscountProduct("Ice MIIIIIIIILK", 50, 30, 0.5)
    print(milk)
    print(bread)
    print(ice_cream)
    print("There are ", str(DiscountProduct.storage_product_number), " products in storage")


if __name__ == "__main__":
    main()

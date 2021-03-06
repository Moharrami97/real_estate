from abc import ABC


class Rent(ABC):
    def __init__(self, initial_price, monthly_price, convertable, discountable, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(
            f"price: {self.initial_price} \t discountable: {self.discountable}"
            f" \t convertable: {self.convertable}"
        )


class Sale(ABC):
    def __init__(self, price_per_meter, convertable, discountable, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.convertable = convertable
        self.discountable = discountable
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(
            f"price: {self.price_per_meter} \t discountable: {self.discountable}"
            f" \t convertable: {self.convertable}"
        )

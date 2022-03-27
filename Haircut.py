class Haircut():
    """
    Haircuts with a name, price, and weekly frequency of purchase
    """
    def __init__(self, name: str, price: float, frequency: int):
        """
        Initialization function for a type of haircut
        :param name: name of haircut
        :param price: price of haircut
        :param frequency: number of haircuts last week
        """
        self.name = name
        self.price = price
        self.frequency = frequency

    def __repr__(self):
        return f'Haircut({self.name},{self.price},{self.frequency})'

    def change_price(self, netchange: float) -> float:
        """
        Change the price of a specific haircut
        :param netchange: positive/negative value to change price by
        :return: Updated/new price
        """
        self.price = self.price + netchange
        return self.price

    def weekly_rev(self) -> float:
        """
        Generate the weekly revenue of any single haircut
        :return: haircut revenue
        """
        weekly_rev = self.price * self.frequency
        return weekly_rev

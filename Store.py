from Haircut import Haircut

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 35, 50]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

class Store:
    def __init__(self, hairstyles, prices, last_week):
        self.haircuts = self.haircutcreate(hairstyles, prices, last_week)

    def haircutcreate(self,hairstyles, prices, last_week):
        haircuts = list()
        for i in range(len(hairstyles)):
            h = Haircut(hairstyles[i], prices[i], last_week[i])
            haircuts.append(h)
        return haircuts

    def averageprice(self):
        totalprice = 0
        for x in self.haircuts:
            totalprice += x.price
        averageprice = totalprice / len(self.haircuts)
        print("The average price of the haircuts is: " + str(averageprice))
        return averageprice

    def total_revenue(self):
        total_rev = 0
        for x in self.haircuts:
            total_rev += x.weekly_rev()
        print("The total revenue this week is: " + str(total_rev))
        return total_rev

    def cheap_haircuts(self):
        cheap_haircuts = list()
        for x in self.haircuts:
            if x.price < 30:
                cheap_haircuts.append(x)
        print(cheap_haircuts)
        return cheap_haircuts


store1 = Store(hairstyles, prices, last_week)

avg_price = store1.averageprice()
total_rev = store1.total_revenue()
#create new list of haircuts under $30
cheap_haircuts = store1.cheap_haircuts()
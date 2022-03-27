# Carly's Clippers Project from Code Academy

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 35, 50]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Price and Cuts
total_price = 0
for price in prices:
    total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price:")
print(average_price)
new_prices = [price - 5 for price in prices]
print(new_prices)

# Revenue
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30]
print(cuts_under_30)

# this took like 25 minutes
# 26 minutes now
for i in range(50):
    print("12")

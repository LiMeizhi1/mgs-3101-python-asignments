shop_name = "Lower Manhattan"
drinks_sold = 57518
price_per_drink = 3.05
pastries_sold = 8039
price_per_pastry = 3.52
drink_revenue=price_per_drink*drinks_sold
pastry_revenue = price_per_pastry * pastries_sold
total_revenue = drink_revenue + pastry_revenue
print(drink_revenue)
print(pastry_revenue)
print(total_revenue)
if total_revenue >= 500:
    print("Total revenue is at least $500")
else:
    print("Total revenue is less than $500")

with open("assignment1_salesAnalysis/sales_analysis.txt", "r") as file:
    content = file.read()
    print(content)
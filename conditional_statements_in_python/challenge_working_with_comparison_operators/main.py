# Item costs
apples_price = 15
oranges_price = 25
bananas_price = 15

# Check if apples and bananas have the same cost
is_same_price = apples_price == bananas_price

# Check if the combination of apples and oranges is cheaper than oranges and bananas
is_cheaper_combination = (apples_price+oranges_price)<(oranges_price+bananas_price)

# Testing 
print("The result of the first comparison:", is_same_price)
print("The result of the second comparison:", is_cheaper_combination)
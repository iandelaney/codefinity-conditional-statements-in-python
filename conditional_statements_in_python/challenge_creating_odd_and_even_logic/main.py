# Initial variables and values
num = 8941 % 931
result = 'blank'

# Determine whether the number is odd or even
if num % 2 == 0:      # ← change here: test remainder, not equality to 0
    result = "even"
else:
    result = "odd"

# Testing
print("The number num is", result)
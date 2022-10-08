weight = 200

# ground shipping layount
#  elif weight <= :
#   cost = weight *  + 20.00
#   print(cost, "is your total")

# ground shipping premium

# 'Ground Shipping'
if weight <= 2:
    cost = weight * 1.50 + 20.00
    print(cost, "is your total")
elif weight <= 6:
    cost = weight * 3.00  + 20.00
    print(cost, "is your total")
elif weight <= 10:
   cost = weight * 4.00 + 20.00
   print(cost, "is your total")
elif weight > 10:
   cost = weight * 4.75 + 20.00
   print(cost, "is your total")

# ground shipping premium

if weight > 0:
    cost = weight + 125.00
    print(cost, "is your total cost")

# drone shipping 
# 'Ground Shipping'
if weight <= 2:
    cost = weight * 4.50 + 20.00
    print(cost, "is your total")
elif weight <= 6:
    cost = weight * 9.00  + 20.00
    print(cost, "is your total")
elif weight <= 10:
   cost = weight * 12.00 + 20.00
   print(cost, "is your total")
elif weight > 10:
   cost = weight * 14.25 + 20.00
   print(cost, "is your total")

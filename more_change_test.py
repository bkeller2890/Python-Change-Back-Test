
print()
change = float(input("Please Insert Change in dollars and cents: $"))

price = float(input("Purchase Price: $"))
print(f"Product costs ${price:.2f}" )

while change < price: 
     
     more_change = float(input("Please insert more change in dollars and cents: $"))

     change += more_change

     if change == price: 
         print("Purchase completed")
         break 
#note - the error here is even if you get to even change - 

if change > price: 
   c_back = change - price
   print(f"You get ${c_back:.2f}in change back")
   print("Purchase Completed")


else:
   print("Exact Change, no change back")
   print("Purchase Completed\n")

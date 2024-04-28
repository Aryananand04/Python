#please give inputs only in CAPSLOCK
print("Thank you for choosing Python Pizza Deliveries!\n")
print("What size pizza do you want? 'S', 'M', or 'L'\n")
size = input()
print("Do you want pepperoni? 'Y' or 'N'\n")
add_pepperoni = input()  
extra_cheese = input()  

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
# format specifiers = {value:flags} format a value based on what
#                     flags are inserted

# .(number)f = round that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to left more position
# :  = insert a space before positive numbers
# :, = comma seperator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is £{price1:,}")
print(f"Price 1 is £{price1:,.2f}")
print(f"Price 1 is £{price1:+,.2f}")
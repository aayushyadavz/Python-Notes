x = input("x: ")
y = int(x) + 1  # converting x (string) into int to avoid type error
print(f"x: {x}, y: {y}")

# Python also have:
# float(x)
# bool(x)
# str(x)

# Some values are interpreted as falsy, meaning they are treated as false in a boolean context:
# ""
# 0
# None

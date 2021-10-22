format_tuple = (37.863, 'Brent', 3, 62.887, 1, 11)
format_string = "The price of {name} crude oil fell to $ {num1} per barrel, setting a {num2}-month anti-record. The current price is only {num3}% of last year's {name} oil price on the same day ({num4}.{num5})."
print(format_string.format(name = format_tuple[1], num1 = format_tuple[0], num2 = format_tuple[2], num3 = round(format_tuple[3], 2), num4 = str(format_tuple[4]).zfill(2), num5 = format_tuple[5]))


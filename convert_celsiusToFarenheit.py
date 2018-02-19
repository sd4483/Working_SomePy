def convert_temp(c):
    f=c*9/5 + 32
    if c >= -273.15:
        return f
    else:
        return "Enter valid temperature"

print(convert_temp(-273.16))

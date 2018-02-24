celsius_temperatures = [10,-20,-289,100]
farenheit_temperatures = []
def convert_temp(c=float):
    for temp in celsius_temperatures:
        if temp<-273.15:
            print("The temperature doesn't make sense")
        else:
            f=temp*9/5 + 32
            farenheit_temperatures.append(f)
            print(f)

convert_temp()

def writeTempToFile():
    with open("tempconversion.txt", "a+") as file:
        for j in farenheit_temperatures:
            file.write(str(j)+"\n")
            file.seek(0)
            i = file.readlines()
            for k in i:
                print(k)
writeTempToFile()

#     f=c*9/5 + 32
#     if c >= -273.15:
#         return f
#     else:
#         return "Enter valid temperature"
#
# print(convert_temp(-273.16))

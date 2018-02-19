#print(int(2,5))
# print(2,5)
# i = (2.5,6)
# print(i)
# print(2/0) #Gives a Zero Division Error

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError: #Can also just write except, but not a good programming practice
        return "Don't give zero, idjit"

print(divide(1,2)) #Executes perfectly
print(divide(1,0)) #Zero Division Error, the exception code is executed

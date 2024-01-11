a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
try:
    c=a/b
except:
    c=a/(b+2)
    print("Division by zero not permitted")
    print(c)
a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
try:
    c=a/b
except:
    c=a/(b+2)
    print("division by zero not permitted")
else:
    print("No exceptions generated")    
finally:
    print("Result is",c)
def square(x):
    return x**2

print("The output is :",square(10))


s= lambda x:x**2
print(s(5))


numbers=[1,2,3,4,5]
#using a lambda function with map to square each element
squared_numbers = map(lambda x:x**2, numbers)

print(list(squared_numbers))
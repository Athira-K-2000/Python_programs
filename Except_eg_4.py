name=input("Enter your name :")
age=int(input("Enter your age :"))
if age<18:
    raise Exception("You should be atleast 18 years old to enroll in voters list")
else:
    print(name,"is enrolled in voters list")
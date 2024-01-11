try:
    num=int(input("Enter the number :"))
    i=1
    fact=1
    if num==1 or num ==0:
        print("factorial is 1")
        
    else:
        while i<=num:
            fact=fact*i
            i+=1
        print(fact)

except:
    if num<0:
        raise Exception("negative number not have factorial")

def list_except():

    try:
        a = []
        n = int(input("enter the limit :"))
        print("Enter the numbers :")
        for i in range(0,n):
            e=int(input())
            a.append(e)
        index=int(input("Enter the index :"))
        print(a[index])

    except IndexError:
        print("Error : Index is out of range")

list_except()


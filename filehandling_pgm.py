#read
filepr = open("sample.txt","r")
if filepr:
    print("open success")


#write
file = open("sample.txt","a")
file.write("........happy coding")
file.close()

'''file = open("sample.txt","w")
file.write("........happy coding")
file.close()'''

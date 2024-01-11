list1=[1,2,3]
list2=['a','b','c']
list3=['x','y','z']

zipped_lists=zip(list1,list2,list3)
result=list(zipped_lists)
print(result)

unzipped_lists=zip(*result)
print(unzipped_lists)

#unzipped_result=[list(item) for item in unzipped_lists]
unzipped_result=[]
for item in unzipped_lists:
    unzipped_result.extend(list(item))
print(unzipped_result)



list_1=['name','age','address']
list_2=['Athira',23,'valanchery']
s=zip(list_1,list_2)
result=dict(s)
print(result)
import functools
#3.
lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
positive_list=[abs(i) for i in lst1]
print(positive_list)
print(list(filter(lambda x:x<0,lst1)))


#4.
def add(a,b):
    print("A=",a,"B=",b)
    return a+b
g=functools.reduce(add,range(1,4))
print("Total=",g)



#5
lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
lst2 = [198, 166, 237, 125]
dictlist=dict(zip(lst1,lst2))
print(dictlist)



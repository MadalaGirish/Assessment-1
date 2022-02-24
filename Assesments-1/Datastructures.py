# 1.Return all the duplicate values from list of arraylis



# 2.Merge two lists as shown below
list1 =["Hello ", "take "]
list2 = ["Dear", "Sir"]

def merge(list1, list2,):
    merged_list =[(list1[i],list2[i]) for i in range(0,len(list1))]
    return merged_list
print(merge(list1,list2))

#3.Example
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub_List=["h", "i", "j"]
list1[2][1][2].extend(Sub_List)
print(list1)

# 4.Map the dictionary in the following manne
Keys = ["Ten","Twenty","Thirty"]
Value = [10,20,30]
print(dict(zip(Keys,Value)))
# 5.Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
def Merge(dict1,dict2):
    res = dict1 | dict2
    return res
dict3 = Merge(dict1,dict2)
print(dict3)

# 6.Rename key city to location in the following dictionary
sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york" }
new_key="Location"
old_key="city"
sampleDict[new_key]=sampleDict.pop(old_key)
print(sampleDict)

#7.Convert Dictionary to list
#Theorigina  : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}


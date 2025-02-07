#1.sort the nested array by value
dict1={'child1':{'name':'agathi','age':26},'child2':{'name':'dhanushiya','age':24},'child3':{'name':'aalai','age':21}}
items=list(dict1.items())
print(items)
for i in range(len(items)-1):
    for j in range(len(items)-i-1):
        if items[j][1]['name']> items[j+1][1]['name']:
            items[j],items[j+1]=items[j+1],items[j]
sorted_items={}
for key,value in items:
    sorted_items[key]=value
print(sorted_items)
print(dict(items))
# ----------------------------------------------------------------------------------------------------------------------
#2.sort the nested array by value using lambda function
sorted_dict=dict(sorted(dict1.items(),key=lambda item:item[1]['name']))
print(sorted_dict)
for key,value in dict1.items():
    for i in value:
        print(key)
    for x in value:
        print(x,value[x])
# ----------------------------------------------------------------------------------------------------------------------
#3.Convert dictionary items into a list of tuples
items = list(dict1.items())

# Sorting using a nested loop (Bubble Sort)
for i in range(len(items) - 1):
    for j in range(len(items) - i - 1):
        if items[j][1]['name'] > items[j + 1][1]['name']:
            items[j], items[j + 1] = items[j + 1], items[j]  # Swap elements
#-----------------------------------------------------------------------------------------------------------------------
#4.Write a Python script to add a key to a dictionary.
dict1.update({'child4':{'name':'selvi','age':"24"}})
print(dict1)
# ----------------------------------------------------------------------------------------------------------------------
#5.Write a Python script to concatenate the following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4={}
print(dic4)
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)
# ----------------------------------------------------------------------------------------------------------------------
#6.Write a Python program to iterate over dictionaries using for loops.
for key,value in dic4.items():
    print(key,":",value)
# ----------------------------------------------------------------------------------------------------------------------
#7.Write a Python script to merge two Python dictionaries.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic1.update(dic2)
print(dic1)
for i in range(5,7):
    dic1[i]=i*10
print(dic1)
# ----------------------------------------------------------------------------------------------------------------------
#8.Write a Python program to remove a key from a dictionary.
dic1={1:10, 2:20,3:30,4:40}
dic1.pop(2)
dic1.popitem()
print(dic1)
# ----------------------------------------------------------------------------------------------------------------------
#9.Write a Python program to sum all the items in a dictionary.
sum_dict={'tamil':70,'english':80,'maths':90}
sum=0
for i in sum_dict.values():
    sum+=i
print(sum)
# ----------------------------------------------------------------------------------------------------------------------
#10.Write a Python program to sort a given dictionary by key.
dict={1:10,2:20,3:30,4:40,5:50,6:50}
for i,j in sorted(dict.items()):
    print(i ,":",dict[i])
#     ----------------------------------------------------------------------------------------------------------------------
#11.Write a Python program to get the maximum and minimum values of a dictionary.
max=dict[1]
for i in dict.values():
    if i>max:
        max=i
print(max)
min=dict[1]
for i in dict.values():
    if i<min:
        min=i
print(min)
# ----------------------------------------------------------------------------------------------------------------------
#12.Write a Python program to remove duplicates from the dictionary.
res={}
for key,value in dict.items():
    if value not in res.values():
        res[key]=value
print(res)
# ----------------------------------------------------------------------------------------------------------------------
#13.Write a Python program to check if a dictionary is empty or not.
dict={}
if dict:
    print("is not empty")
else:
    print("empty")
#----------------------------------------------------------------------------------------------------------------------
#14.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=d1.copy()
for key in d2.keys():
    if key in d1:
        d3[key]=d1[key]+d2[key]
    else:
        d3[key]=d2[key]
print(d3)
# ----------------------------------------------------------------------------------------------------------------------
#15.Write a Python program to print all distinct values in a dictionary.
data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
uni=[]
for dic in data:
    for key,value in dic.items():
        if value not in uni:
            uni.append(value)
print(uni)
# ----------------------------------------------------------------------------------------------------------------------
#16.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
data ={'1':['a','b'], '2':['c','d']}
res=[]
for key,value in data.items():
    for i in value:
        res.append(i)
for i in res:
    for j in res:
        if i != j:
            print(i+j)

print(res)
# ----------------------------------------------------------------------------------------------------------------------
#17.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
dict1={'child1':{'name':'agathi','age':26},'child2':{'name':'dhanushiya','age':24},'child3':{'name':'kalai','age':21},'child4':{'name':'aalai','age':20}}
dic=list(dict1.items())
print(dic)
sum=0
for i in range(len(dic)-1):
    for j in range(len(dic)-i-1):
        sum+=dic[j][1]['age']
print(sum)

age_list = [(key, value['age']) for key, value in dict1.items()]
#----------------------------------------------------------------------------------------------------------------------
#18.Sorting the list based on age in descending order and get the highest 3 values
for i in range(len(age_list) - 1):
    for j in range(len(age_list) - i - 1):
        if age_list[j][1] < age_list[j + 1][1]:  # Descending order
            age_list[j], age_list[j + 1] = age_list[j + 1], age_list[j]
top_3 = age_list[:3]
top_3_dict = {key: dict1[key] for key, age in top_3}
print(top_3_dict)
#----------------------------------------------------------------------------------------------------------------------
#19.Write a Python program to create a dictionary from a string.
sample_string='w3resource'
res={}
for i in sample_string:
    res[i]=sample_string.count(i)
print(res)
# ----------------------------------------------------------------------------------------------------------------------
#20.Write a Python program to count the values associated with a key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
sum=0
for d in student:
    sum+=d['id']
print(sum)
# ----------------------------------------------------------------------------------------------------------------------
#21.Write a Python program to get the top three items in a shop.
data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
res=list(data.values())
data1={}
res.sort()
print(res)
for i in res:
    for key,value in data.items():
        if i==value:
            data1[key]=i
print(data1)
# ----------------------------------------------------------------------------------------------------------------------
#22.write a program to convert a json to dictionary
import json
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print(employee)
print(type(employee))
employee_dict=json.loads(employee)
print(employee_dict)
print(type(employee_dict))
#23.write a program to convert dictionary to json
employee_json=json.dumps(employee_dict)
print(employee_json)
print(type(employee_json))
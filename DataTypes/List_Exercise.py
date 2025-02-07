# 1.Write a Python program to find the length of a list.
a=[1,2,3,4,5,6,7]
length=len(a)
print(length)
# ---------------------------------------------------------------------------------------------------------------------
#2.Write a Python program to add an element to the end of a list.
a.append(7)
print(a)
# ---------------------------------------------------------------------------------------------------------------------
#3.Write a Python program to add an element to the beginning of a list.
a.insert(0,8)
print(a)
# ---------------------------------------------------------------------------------------------------------------------
#4.Write a Python program to insert an element at a specific index in a list.
a.insert(7,20)
print(a)
# ---------------------------------------------------------------------------------------------------------------------
#5.Write a Python program to remove an element from the end of a list.
a.pop()
print(a)
# ---------------------------------------------------------------------------------------------------------------------
#6.Write a Python program to remove an element from the beginning of a list.
#7.Write a Python program to remove an element at a specific index in a list.
a.pop(0)
print(a)
# ---------------------------------------------------------------------------------------------------------------------
#8.Write a Python program to reverse a list.
# a.reverse()
print(a[::-1])
a.sort(reverse=True)
# ---------------------------------------------------------------------------------------------------------------------
#9.Write a Python program to find the sum element in a list.
sum=0
for i in a:
    sum+=i
print(sum)
# ---------------------------------------------------------------------------------------------------------------------
#10.Write a Python program to find the maximum element in a list.
max=a[0]
for i in a:
    if i>max:
        max=i
# ---------------------------------------------------------------------------------------------------------------------
#11.Write a Python program to find the minimum element in a list.
print(max)
min=a[0]
for i in a:
    if i<min:
        min=i
print(min)
# ---------------------------------------------------------------------------------------------------------------------
#12.Write a Python program to check if a list is empty.
b=[]
if b:
    print("not empty")
else:
    print("empty")
# ---------------------------------------------------------------------------------------------------------------------
#13.Write a Python program to copy a list.
c=a.copy()
c.extend(a)#adding  a list
print(c)
# ---------------------------------------------------------------------------------------------------------------------
#14.Write a Python program to find the intersection of two lists.
l1=[1,2,3,4,5,6,7]
l2=[7,8,9,3,4,5,6]
l3=[]
for i in l2:
    if i in l1:
        l3.append(i)
print(l3)
# ---------------------------------------------------------------------------------------------------------------------
#15.Write a Python program to find thesecond largest number
large=float('-inf')
second_large=float('-inf')
for i in l1:
    if i>large:
        second_large=large
        large = i
    elif i!=large and i>second_large:
        second_large=i
print(second_large)
temp=0
for i in range(0,len(l1)-1,2):
    temp=l1[i]
    l1[i]=l1[i+1]
    l1[i+1]=temp

print(l1)















import copy

a = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the nested list 'original'
b = copy.deepcopy(a)

# Modifying an element in the shallow-copied list
b[0][0] = 99

# Printing the original and shallow-copied lists
print(b)
print(a)
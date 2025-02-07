n=('kalai','selvi','k','dhanu','agathiyan','kalai')
# 1.write a program to count the value in tuple
print(n.count('kalai'))
# ---------------------------------------------------------------------------------------------------------------------
# 2.write a program to find the index of the value
print(n.index('dhanu'))
# ---------------------------------------------------------------------------------------------------------------------
#3.write a program to unpack a tuple
a=(1,2,3,4)
n1,n2,n3,n4=a
print(n1+n2+n3+n4)
# ---------------------------------------------------------------------------------------------------------------------
#4.Write a Python program to add an item to a tuple.
b=list(a)
b.append(5)
print(tuple(b))
# ---------------------------------------------------------------------------------------------------------------------
#5.Write a Python program to convert a tuple to a string.
tuple_to_str=' '.join(n)
print(tuple_to_str)
# ---------------------------------------------------------------------------------------------------------------------
#6.Write a Python program to add member(s) to a set.
set1={'kalai','dhanu','agathiyan','lakshumi'}
set1.add('veldurai')
print(set1)
# ---------------------------------------------------------------------------------------------------------------------
#7.Write a Python program to remove item(s) from a given set.
set1.remove('kalai')
print(set1)
# ---------------------------------------------------------------------------------------------------------------------
#8.Write a Python program to remove an item from a set if it is present in the set.
set1.discard('dhan')
print(set1)
# ---------------------------------------------------------------------------------------------------------------------
#9.Write a Python program to create an intersection of sets.
set2={'kalai','dhanu','agathiyan','lakshumi','abinaya','kishore'}
set3=set1.intersection(set2)
print(set3)
# ---------------------------------------------------------------------------------------------------------------------
#10.Write a Python program to create a symmetric difference.
set4=set1^set2
print(set4)
# ---------------------------------------------------------------------------------------------------------------------
#11.Write a Python program to check if a set is a subset of another set.
set5=set2.issubset(set1)
print(set5)
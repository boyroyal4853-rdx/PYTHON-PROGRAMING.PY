# set => it is a collection .

# => it is unordered .
# => it is unindexed .
# => it can not containe duplicate elements .
# => it can store only unique elements .
# => it is mutable .



listt = [11, 22, 33, 44, 55]
tuplet = (11, 22, 33, 44, 55)

sett = {11, 22, 33, 44, 55}

my_set = {11, 22, 33, 44, 55, 11, 22, 33}
# Dulicate elements => 11,22,33
print("this is actual elements of this set :", my_set)


# set methods:-

# 1. add () :- it is used to add single element in the set .

my_set = {11, 22, 33, 55, 44, 2}
print("before adding element :", my_set)

my_set.add(77)
print("after adding element  :", my_set)

# 2. update() :- it is used to add  multiple elements in the set.

my_set = {11, 22, 33, 55, 44, 2}
print("before adding element :", my_set)

my_set.update({77, 999,102})
print("after adding element  :", my_set)


# 3. remove()  => it is used to remove specific element from the set.


my_set = {11, 22, 33, 55, 44, 2}
print("before adding element :", my_set)

my_set.remove(22)
print("after adding element  :", my_set)




my_set = {11, 22, 33, "rahul", "ravi" , 8.8}
print("before adding element :", my_set)

print(my_set[4]) ## set data structure does not support indexing






my_set = {11, 22, 33, "rahul", "ravi" , 8.8}
print("before adding element :", my_set)

for i in my_set:
    print(i)


# pop() = > it is used to remove random element from the set.


my_set = {11, 22, 33, "rahul", "ravi" , 8.8}
print("before adding element :", my_set)
my_set.pop()
print("after poping element  :", my_set)

# discard()
# => it is used to remove specific element from the set .
# => it does not raise error if the element is not found in the set .


my_set = {11, 22, 33, "rahul", "ravi" , 8.8}
print("before adding element :", my_set)
my_set.discard(224565432)
print("after poping element  :", my_set)


 # clear() 
# => it is used to remove all elements from the set .



my_set = {11, 22, 33, "rahul", "ravi" , 8.8}
print("before adding element :", my_set)
my_set.clear()
print("after poping element  :", my_set)





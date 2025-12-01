          #  0     1   2    3   4
my_tuple = (99,22, 32, 420, 502)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[4])

my_tuple = (122, 222, 322, 42, 52)
print(my_tuple)

for i in my_tuple:
    print(i)

## # Tuple MEthods:-
# # 1. count()  => it return the number of occurrence of any element. 

my_tuple = (111, 111, 111, 22, 7879)
print(my_tuple.count(111)) 


# # 2. index() => it returns the index of first occurrence of any element.


my_tuple = (111, 111, 111, 22, 7879)
print(my_tuple.index(111)) 

# 3. length() => it returns the number of elements in a tuple.


my_tuple = (111, 111, 111, 22, 7879)
print(len(my_tuple)) 



            # 0     1   2    3   4
my_tuple = (122, 222, 322, 42, 52)
print(my_tuple[3])  

# Negtive Indexing :-

my_tuple = (333, 222, 111, 422, 52)
          # -5   -4  -3    -2  -1
 
print(my_tuple[-2] ) 

# # tuple: -
# # => A tuple is a collection which is immutable and ordered.
# # => it can not be changed after creation.


my_tuple = (122, 222, 322, 42, 52)
print(my_tuple)


my_tuple = (111, 111, 111, 22, 7879)
print(len(my_tuple)) 

# #           0   1   2   3   4
# # listt = [11, 22, 33, 44, 55]
# # Immutable , Mutable
# # ( ) => Parenthesis
# # [ ] => Square brackets
# # { } => Curly braces
# # Mutable OR Changeable:

# # => it can be changed entirely as well as specifically.
# # Example:  List, Dictionary, Set

# # Immutable OR Unchangeable:

# # => it can be changed entirely but not specifically.
# # Example:  Tuple, String, Frozen Set

      #  0   1   2   3   4
listt = [11, 22, 33, 44, 55]
print("before changes :", listt)

listt[2] = 777
print("after changes  :", listt)

# String Immutable

my_name = "krishna"
print("before changes :", my_name)

print(my_name[0])  




my_name = "god morning"
print("before changes :", my_name)

print(my_name[0])  # g

my_name[0] = "G"  # Error
print("after changes  :", my_name)


name = "Ram"
print("before changes :", name)

name = "Shyam"
print("after changes:",name)
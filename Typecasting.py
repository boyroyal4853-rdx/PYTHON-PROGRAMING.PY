# 📌 TYPECASTING
# Typecasting = Converting one data type into another
# Types of Typecasting in Python
# 1️⃣ Explicit Typecasting
# 2️⃣ Implicit Typecasting


# 1️⃣ Explicit Typecasting
# (Developer converts manually)
# String → Integer
my_variable = "23"
print(type(my_variable))

my_new_variable = int(my_variable)
print(my_new_variable)
print(type(my_new_variable))



23
# <class 'int'>

# Integer → String
my_variable = 23
print(type(my_variable))

my_new_variable = str(my_variable)
print(my_new_variable)
print(type(my_new_variable))





# Output
# <class 'int'>
# 23
# <class 'str'>



# Boolean → Integer
my_variable = True
print(type(my_variable))

my_new_variable = int(my_variable)
print(my_new_variable)
print(type(my_new_variable))




# Integer → Boolean
my_variable = 1
print(type(my_variable))

my_new_variable = bool(my_variable)
print(my_new_variable)
print(type(my_new_variable))





# ✔ Rule:
# bool(non-zero number) → True  
# bool(0) → False

my_variable = 0
print(type(my_variable))

my_new_variable = bool(my_variable)
print(my_new_variable)
print(type(my_new_variable))






# [2]** Implicit Typecasting
# (Python automatically converts)
my_variable = 6.7
my_second_variable = 4

print(type(my_variable))          
print(type(my_second_variable))   

print("after implicit typecasting:", my_variable + my_second_variable)





# ➡ int + float → float automatically

# 🧾 DICTIONARY INTRODUCTION
# A dictionary stores data in key-value pairs
#  ✔ mutable
#  ✔ ordered
#  ✔ keys must be unique and immutable

# Example
my_dict = {
    "name": "Ujwal",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(my_dict)






# Key = Left side
# Value = Right side
# Example:



my_listt = [11, 22, 33, [5, 6, 7], 55]
print(my_listt)


# 📌 Difference:
#  List stores only values
#  Dictionary stores key + value together
#



for i in range(10):
   print("Radhe-Radhe")

x = 20
for i in range(x):
       print(i)

a = int(input("Enter a : "))
for i in range(a):
    print(i)
    
    z = int(input("Enter i: "))
for i in range(z):
    print("python",i)

for i in range(5,15):
    print(i)  

for i in range(5,51,5):
   print(i)

a_=int(input("enter n"))
b=int(input("enter m"))
c=int(input("enter s"))

for i in range(a,b,c):
    print(i)

# 1. Basic Range
for i in range(5):
    print("first output", i)

start = 0 #(default)
end = 5 #(excluded)


#
# 2. Range (0,5)
for i in range(0,5):
    print("second output", i)



# 3. Range (13,18)
for i in range(13,18):
    print(i)


# 4. Range (22,27)
for i in range(22,27):
    print(i)


# 5. Slicing Example
listt = [22,21,23,33,44,55]
print(listt[0:3])


# 6. Gap Example
print(listt[0:5:2])




# 7. Even Numbers
for i in range(2,21,2):
    print(i)



# 8. Multiples of 5
for i in range(5,51,5):
    print(i)


# 9. Negative to Positive
for i in range(-2,5):
    print(i)


# 10. Your last example
for i in range(9,23,1):
    print("first output", i)

for i in range(9,23):
    print("second output", i)





#     For Loop (C + Python Complete Breakdown)
# Example Code (C):
# for(int i = 0; i < 5; i++){
#     printf("%d", i);
# }


# ⭐ STEP-BY-STEP PROCESS (General Explanation)
# Initialization → i = 0 (Loop variable create hota hai)


# Condition Check → i < 5


# Task Perform → printf(i)


# Increment → i++ (i = i + 1)



# ⭐ PHASE-WISE EXECUTION
# PHASE 1
# initialization → i = 0


# condition check → 0 < 5 → TRUE


# perform task → print(0)


# increment → 0++ → i = 1



# PHASE 2
# initialization → i = 1


# condition check → 1 < 5 → TRUE


# perform task → print(1)


# increment → 1++ → i = 2



# PHASE 3
# initialization → i = 2


# condition check → 2 < 5 → TRUE


# perform task → print(2)


# increment → 2++ → i = 3



# PHASE 4
# initialization → i = 3


# condition check → 3 < 5 → TRUE


# perform task → print(3)


# increment → 3++ → i = 4



# PHASE 5
# initialization → i = 4


# condition check → 4 < 5 → TRUE


# perform task → print(4)


# increment → 4++ → i = 5



# PHASE 6
# initialization → i = 5


# condition check → 5 < 5 → FALSE


# Condition FALSE → Loop EXIT






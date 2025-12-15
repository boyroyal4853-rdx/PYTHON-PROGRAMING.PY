# Nested loop :-
# => loop inside another loop.


# for i in range(0,2):
#          for i in range(0,1):
#              print("the value of i : ", i )
             


# for i in range(0,4):
#                  print(i)
#                  print("SHivam")

# 1. initialization : i = 0
# starting point = 0
# ending point = 4

# 2. condition check
# codition (i < 4)

# 3. execute some lines of code.
# print(------------------)

# 4. increment i by 1
#         i++




# for i in range(0,2):
#          for j in range(0,5):
#              print("the value of i : ", i, "the value of j", j )
             

# phase 1:
# 1. initialization, i = 0
# 2. condition check , (i < 2), 0 < 2 => TRUE
# 3. execute some lines of code 


# phase a:
# 1. initialization ,  j = 0
# 2. condition check , (j < 1)  , 0 < 1 => TRUE
# 3. execute some lines of code 
# 4. j increment by 1 =>    , j++ , 0++ => j = 1

# phase b:
# 1. initialization ,  j = 1
# 2. condition check , (j < 1)  ,  1 < 1 => FALSE 
# exit from the loop

# phase 1:   
# 4. i increment by 1 .   i++,  0++ => 1



# phase 2:
# 1. initialization, i = 1
# 2. condition check , (i < 2), 1 < 2 => TRUE
# 3. execute some lines of code 

# phase a:
# 1. initialization: j = 0
# 2. condition check , ( j < 1 ) , 0 < 1 => TRUE
# 3. execute some lines of code 
# 4. j increment by 1,   j++

# phase b :
# 1. initialization : j = 1
# 2. condition check , ( j < 1) , 1 < 1 => False 
# exit from the loop


# phase 2 : 
# 4. i increment by 1 ,   i ++,    1++ => 2


# Phase 3:
# 1. initialization :  i = 2
# 2. codition check , (i < 2 ), 2 < 2 => False 
# => exit from the loop
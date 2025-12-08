# Jump statement 
# 1. break 
# 2. continue

# break statement => when the provided condition is true , then it exits from the loop instantly.


for i in range(0, 12):
                    if i == 7:
                                 break
                    print(i)


# continue => it skips the current iteration , and move to the next iteration

# => if the given the condition is true then it skips only that part and move to the next.

for i in range(0, 12):
                    if i == 7:
                               continue
                    print(i)




# #              0      1     2   3   4
my_listt = ["Ravi","rohit", 44, 55, 88]

for i in my_listt:
                    if i == 44:
                                        break
                    print(i)




my_listt = ["Ravi","rohit", 101, 44, 55, 88]

for i in my_listt:
                    if i == 101:
                                        break
                    print(i) 



my_listt = ["Ravi","rohit", 101, 44, 55, 88]

for i in my_listt:
                    if i == 101:
                                        continue
print(i)
a = float(input("Enter first number: "))
b = float (input("Enter second number: ") )
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)    
if op == "-":
    print("Result =", a - b)
if op == "*":
    print("Result =", a * b)
if op == "/":
    print("Result =", a / b)
else:
    
    print("Invalid operator")

   
age= 17
resident = "india"

if age >18 :
    print("you are voter in indian election" )
elif resident == "indian":
    print("you are indian citizen")
else:
    print("you are not eligible to vote in indian elections")

x=5
y=2      

if x>y :
    print("x is greater than y")
else:
    print("y is greater than x")

#
    # 🏫 Program 1: Chek Voting Eligibility Using Nested
age = int(input("hii, Shivam! plesae enter your age"))

resident  = "Bihar"

if age > 18 :

     if resident == "Bihar":
                   print("you are eligible to vote")
     else:
                   print("sorry, you are not eligible to vote, becuase you are not resident of Bihar")
else:
                   print("you are not eligible to vote")


# 🏫 Program 2: Chek Loan Eligibility Using Nested
civil_score = int(input("Hii, Ravi! please enter your civil score"))
income = int(input("hii, Ravi! enter your income"))

if civil_score > 750:
                   if income > 350000 :
                                       print("congrats , you can apply home load from SBI bank")
                   else:
                                       print("sorry , you can't get a loan, because you income is very low")
                  
else:
              print("according to the Bank policy , you account is eligible to get a loan")





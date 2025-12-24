#FIRST PILER OF OOPS .
#  1 INHEIRTENCE:>  Inheritance is a fundamental concept in object-oriented programming (OOP)allows 
#                     where a class can inherit attributes and methods from another class. This for
#                     code reusability and the creation of hierarchical relationships between classes.                                                                    




#SINGLE INHEIRTENCE

class  father:
       bussiness = " UNIQUE FASHION HUB"        
       bussiness_investment = "20L"
       house_price = "15L"
       car_price = "8L"
       bike_price = "2L"
       bamk_balance = "5L"
       total_property = "50L"

class son(father):
        job =  " SOFTWARE DEVELOPER"      
        salary = "80k"
        bank_save = "10L" 
        
my_obj = son()
print(" BUSINESS NAME  :", my_obj.bussiness)
print(" BUSINESS INVESTMENT  :", my_obj.bussiness_investment)
print(" HOUSE PRICE  :", my_obj.house_price)   
print(" CAR PRICE  :", my_obj.car_price)
print(" BIKE PRICE  :", my_obj.bike_price)
print(" BANK BALANCE  :", my_obj.bamk_balance)
print(" TOTAL PROPERTY  :", my_obj.total_property)
print(" JOB  :", my_obj.job)
print(" SALARY  :", my_obj.salary)
print(" BANK SAVE  :", my_obj.bank_save)

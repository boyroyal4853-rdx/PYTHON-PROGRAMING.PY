#FIRST PILER OF OOPS .
#  1 INHEIRTENCE:>  Inheritance is a fundamental concept in object-oriented programming (OOP)allows 
#                     where a class can inherit attributes and methods from another class. This for
#                     code reusability and the creation of hierarchical relationships between classes.                                                                    

                    # => Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class), promoting code reuse and establishing a clear hierarchy.


# 1 .SINGLE INHEIRTENCE

# class  father:
#        bussiness = " UNIQUE FASHION HUB"        
#        bussiness_investment = "20L"
#        house_price = "15L"
#        car_price = "8L"
#        bike_price = "2L"
#        bamk_balance = "5L"
#        total_property = "50L"

# class son(father):
#         job =  " SOFTWARE DEVELOPER"      
#         salary = "80k"
#         bank_save = "10L" 
        
# my_obj = son()
# print(" BUSINESS NAME  :", my_obj.bussiness)
# print(" BUSINESS INVESTMENT  :", my_obj.bussiness_investment)
# print(" HOUSE PRICE  :", my_obj.house_price)   
# print(" CAR PRICE  :", my_obj.car_price)
# print(" BIKE PRICE  :", my_obj.bike_price)
# print(" BANK BALANCE  :", my_obj.bamk_balance)
# print(" TOTAL PROPERTY  :", my_obj.total_property)
# print(" JOB  :", my_obj.job)
# print(" SALARY  :", my_obj.salary)
# print(" BANK SAVE  :", my_obj.bank_save)




#  MULTIPLEINHEIRTENCE:

# class father:
#        bussiness = " UNIQUE FASHION HUB"

# class mother:
#         cake_beakry  = "SARSWATI CAKE POINT"



# class son(father, mother):
#        job =  " SOFTWARE DEVELOPER"      
#        salary = "80k"
#        bank_save = "10L" 



# multi_obj = son()
# print("FATHER BUSSINESS  =>" , multi_obj.bussiness)
# print("MOTHER BUSSINESS =>"  , multi_obj.cake_beakry)
# print("SON JOB = >" , multi_obj.job )
# print("SON SALARY =>" , multi_obj.salary )
# print("SON BANK SAVE =>" , multi_obj.bank_save )



# MULTILE LEVEL INHEIRTENCE:

# class HOD:
#        post = "HEAD DIRECOTER OF COLLAGE"

# class FACULTY (HOD):
#        faculty_post = "TEACH'S TO ALL STUDENTS"  
# class CR(FACULTY):
#         cr_post = "REPRESENT'S TO ALL STUDENTS"
# class STUDENT (CR):
#        student_post = "LEARN FROM ALL FACULTY"  


# muti_level_obj = STUDENT()
# print(" HOD POST  =>" , muti_level_obj.post)
# print(" FACULTY POST  =>" , muti_level_obj.faculty_post)
# print(" CR POST  =>" , muti_level_obj.cr_post)
# print(" STUDENT POST  =>" , muti_level_obj.student_post)


# HIERARCHICAL INHERITANCE:

# class FATHER:
#        bussiness = " UNIQUE FASHION HUB"        
       
# class SON1(FATHER):       
#         work = "chai tapri "

# class SON2(FATHER):
#         jod = " GOVERNMENT TEACHER"        


# son1_obj = SON1()        
# print(" SON1 BUSSINESS  =>" , son1_obj.bussiness)
# print(" SON1 WORK  =>" , son1_obj.work)


# son2_obj = SON2()
# print(" SON2 BUSSINESS  =>" , son2_obj.bussiness)
# print(" SON2 JOD  =>" , son2_obj.jod)


# HYBRID INHERITANCE:
# class grand_father:
#        land = " 100 ACRE "
# class father:
#        bussiness = " UNIQUE FASHION HUB"

# class mother:
#         cake_beakry  = "SARSWATI CAKE POINT"

# class son(grand_father, father, mother):
#        job =  " SOFTWARE DEVELOPER"      
#        salary = "80k"
#        bank_save = "10L" 


# hybrid_obj = son()
# print(" GRAND FATHER LAND  =>" , hybrid_obj.land)       
# print("FATHER BUSSINESS  =>" , hybrid_obj.bussiness)
# print("MOTHER BUSSINESS =>"  , hybrid_obj.cake_beakry)
# print("SON JOB = >" , hybrid_obj.job )
# print("SON SALARY =>" , hybrid_obj.salary )
# print("SON BANK SAVE =>" , hybrid_obj.bank_save )


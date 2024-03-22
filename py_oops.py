# # ...........oops...................
# #oops in python : mae code reusable , easier to work with large program 
# class Checknum:
#     a = 14  #class attribute   
#     __num = 70  #private attribute with double underscore
#     def evenodd(self,n):      #class method
#         if n % 2 == 0:
#             return "even"
#         else:
#             return "odd"
#     def __Hello():
#         print("hello")
#     # @classmethod #decorators a wide concept 

# c = Checknum()  
# d =c.evenodd(6)
# print(d)
# print(c.a)
# print(Checknum.a)    #can be access easily because it is global and public variable
# print(Checknum.num)  #cannot be access because it is private
# print(Checknum.__Hello())  #same private method

class attributes:
    def func(self,n):
        if n ==1:
            print("1")
        else:
            print("no")
    num = 33
    print(num)
at = attributes()  #at is instance object and attributes() is class object 
at2 = attributes() #class objects only once created of calss name but instance object can be created in numbers  
at.func(1)
at.func(10)


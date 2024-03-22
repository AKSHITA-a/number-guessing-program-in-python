#dictionary questions
#1 : merge two dictionary 
'''
dict1 = {1:"a",2:"b",3:"c"}
Keys = list(dict1.keys())
value = list(dict1.values())
print(Keys)
print(value)

#another approach
dict2 = {1:10,2:49,5:27}
l =[]
for i in dict2.keys():
    l.append(i)
print(l)
print(*dict2) #or by easy approach 

#merge two lists
dict2 = {1:10,2:49,5:27,22:"F",23:"A",20:"B"}
dict3 = {20:"A",22:"F",44:"83",36 :"",39:10}   #not allow duplicate elements lie set
sum = dict2                              #if diff values have same key so update the value into updated key
sum.update(dict3)
print(sum)
#print(dict2)
#print(dict3)
#dict2.update(dict3)
#print(dict2)


#sum all the values of the dictionary 
dict = {1:10,2:49,5:27,22:20}
l =[*dict.values()]
print(sum(l))
#or by iterative method 
sum = 0
for i in dict.values():
    sum += i
print(sum)

#count the frequency of all the values in dictionary 
dict = {1:10,2:49,5:27,22:20,10:10}
count = {}
for i in dict.values():
    if i not in count :
        count[i] = 0
    count[i] +=1

print (count)

def convert1(lst):
    res_dict = {}
    for i in range(0, len(lst), 2):
        res_dict[lst[i]] = lst[i + 1]
    return res_dict
my_list = ['a', 1, 'b', 2, 'c', 3]
print(convert1(my_list))  # Output: {'a': 1, 'b': 2, 'c': 3}

l = [2,32,24,20]
dict = {}
for i in range(0,len(l),2):
    dict[l[i]] = l[i+1]
print(dict)

'''
#combine 2 dictionary and if same keys then add their values
dict1={10:1 , 90:39, 30:44, 20:46}
dict2= {50:14 , 20:30, 38:84, 70:49}
for i in dict2.keys():
    if i in dict1.keys():
        dict1[i] += dict2[i]   
    else :
        dict1[i] = dict2[i]
print(dict1)




# # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# # You may assume that each input would have exactly one solution, and you may not use the same element twice.
# # You can return the answer in any order.
# range_list = int(input("enter total number : "))
# nums = []
# list = []
# target = int(input ("enter the target : "))
# for i in range(range_list):
#     ele = int(input("enter array elements : "))
#     nums.append(ele)
#     for j in range(i+1 ,len(nums)):
#         if nums[i] + nums[j] == target:
#             list.append(i)
#             list.append(j)
#         else : 
#             print("not found the target number sum .")
# print("nums = ",nums , "target = ",target)
# print(list)

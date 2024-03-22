#list question : 
'''
Range = int(input("enter how many numbers you want to store in list : "))
list = []
for i in range(0,Range):
    l = int(input())
    list.append(l)
print ("list : ", list )  


list = ["a","b","f","c","d"]
list2 = [1,35,6,7,85,35]
str1 = ' '.join(list)
str2 = ''.join(map(str,list2))
print(str1)
print(str2)

word = input("enter the number for list but they will store as string type here")
l = word.split(" ")
print(l)


#reverse order
l = [2,45,678,"nitin"]
rev = []
for i in range(len(l)-1,-1,-1):
    rev.append(l[i])
print(rev)


#print negative and positive ele in separate list
l = [2,45,-56,34,-63,34,34,2,-31]
p_list = []
n_list = []
for i in l:
    if i < 0:
        n_list.append(i)
    else :
        p_list.append(i)
print("postive elements list : ",p_list)
print("negative elements list : ",n_list)

#find greatest ele and its index too
b = [2,4,67,100,78,33,35,25,3,20]
b.sort()
for i in b:
    item = b[-1]
    if item == i:
        index = len(b)-1
print(item, "is the greatest element in the\n list : ",b,"at " ,index) 


#another method
l = [3,5,70,32,68,3,6,34]
max = 0
for i in range(0,len(l)):
    if l[i] > max:
        max = l[i]
        index = i
print(max)
print(index)


#find greatest string with key highest count r
words = ["my", "name", "is", "thoerr","and", "i have","superrrrpower"]  
var = " ".join(words)
print(var)
# Count the occurrences of 'r' in the entire string
r_count = var.count("r")
print("Count of 'r':", r_count)
# Create a dictionary to store word frequencies
f = {}
for i in words:
    f[i] = i.count("r")

# Find the word with the highest count of 'r'
max_word = max(f, key=f.get)
print("Word with highest 'r' count:", max_word)

l = [3,5,57,3,33]
b= max(l)
i= l.index(max(l))
print(b)
print("at ",i)

#find 2nd greatest element and index too
l = [3,9,45,57,3,48,33]
max = 0
index = 0
max2 = 0
index2 = 0

for i in range(len(l)):
    if l[i] > max:
        max2 = max
        max =l[i]
        index2 = index 
        index = i
    elif l[i] > max2:
        max2 = l[i]
        index2 = i
print(max2)
print(index2)


#check if list sorted or not
l = [1,45,78,43,68,2,68,57,20]
for i in range(len(l)-1):
    if l[i] <= l[i+1] :
        continue
    else :
        print("your list is not sorted")
    break
else :
    print("list is sorted")


#print sorted list  by iterative not by sorted() function
def sort_list(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
            if  l[j] < l[min_index]:
                min_index = j
        l[i] ,l[min_index] = l[min_index],l[i]
         
l = [1,45,78,43,68,2,68,57,20]
sort_list(l)
print(l)             
    

#list is palindrom or not
list = [1,2,4,2,1]
for i in range(0,len(list)):
    if list[i] != list[len(i)-i -1]:
        is_palindrom = True
    else:
        is_palindrom = False
print(is_palindrom)

list = [1,2,4,2,1]
p_list = []
for i in range(len(list)-1,-1,-1):
    p_list.append(list[i])
print(p_list)
if list == p_list:
    print("true")
else:
    print("false")

'''
#find ele excluding repetition
list = [1,3,5,6,42,10,5,73,2,4,5,3,2,1]
print("total elements  :",len(list)-1)
l2 = set(list)
print("total elements without repetition : ",len(l2)-1)


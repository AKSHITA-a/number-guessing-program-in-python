#python projects 

#sequential search algorithm
numbers = list(range(0,29))
def searchn(list , n):
    flag = False
    for i in list :
        if i == n:
            flag = True
            break 
    return flag

print (searchn(numbers , 3))

n=["helloo world" , "r",35,"hfi"]
for i in n:
   print(i)
l = [23,4,3,32,1,2,31,53]
print(l)
l.remove(3)
print(l)
n.remove("r")
print(n)
l.pop(0)
print(l)
l.append(34)
print(l)
l.insert(3,40)
print(l)

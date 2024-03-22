#questions on data types  :
'''
#1 : print a string in reverse , find length , uppercase , lowercase .
str1 = "myname is anthony uncle"
str2 = " "
print("original string  : ", str1)
for i in range(len(str1)-1, -1 ,-1):
    # print(str1[i],end = "")
    str2 += str1[i]
print("reverse string : ",str2)

# shortest method
print(str1[::-1])
#other 
print("uppercase string : ",str1.upper())
print("lowercase string : ",str1.lower())
print("each word 1st letter will capatalized : ",str1.title())

#2: ararnge string characters such that lowercase letters should come first in another stirng
string = "I have A newly Project now"
s  = str(input())
print(s+32)

string = str(input("enter string :  "))
str1 = " "
for i in string:
    if i.islower():
        str1 += i
for i in string:
    if i.isupper():
        str1 += i
        
print("required string :  " ,str1)


#2: ararnge string characters in each letter such that lowercase letters should come first in another letters
string = str(input("enter string :  "))
b = string.split()
c = []

for i in b:
    lowercase_chars = ''.join([char for char in i if char.islower()])
    uppercase_chars = ''.join([char for char in i if char.isupper()])
    arranged_word = lowercase_chars + uppercase_chars
    c.append(arranged_word)

print("Arranged words:", ' '.join(c))


#3 : count all letters , digits , and symbols from a given string by user
string = "P@#yn26at^&i5ve"

digits = 0
letters = 0
symbols = 0
for i in string:
    if i.isdigit():
        digits += 1
    elif  i.isalpha():
        letters +=1
    else :
       symbols +=1
   
print("digits :" ,digits)
print("letters :",letters)
print("symbol : ",symbols)


#ascii values :
#print("print the ascii value of character by ord function : ",ord("A"))
#print("print the character by their ascii by chr function : ",chr(103))


for i in range(65,91):
    print(chr(i),end = " ")
for i in range(97,123):
    print(chr(i),end = " ")

string = "my name is akshita and i like coding the most i dont kow why but it is the king of my dreams from sometimes "
count =0
for i in string:
    if (i == "a" or i=="e" or i == "i" or i=="o"or i =="u"):
        count += 1
print(count)

#or short method :
a ="heloo there is a person to connect with you"
vowel = 0
const = 0
for i in a:
    if i in "aieouAEIOU":
        vowel +=1
    elif i == " ":
        continue        
    else :
        const += 1
print("vowels : " , vowel)
print("const : ",const )


#check string is pallindrom or not
def pallindrom(a):
    b =""
    for i in range(len(a)-1, -1,-1):
        b += a[i]
    if a==b:
        return "palindrom"
    else:
        return "not palindrom"
res = pallindrom("nitin")
print(res)

#print(a == a[::-1])

#check palindrom or not by iterative method 
s = str(input("enter string "))
print("is ",s ," is palindrom ")
for i in range(0,int(len(s)/2)):
    if s[i] != s[len(s)-i -1]:   
        is_palindrom = "false"
    else:
        is_palindrom = "true"
print(is_palindrom)
'''








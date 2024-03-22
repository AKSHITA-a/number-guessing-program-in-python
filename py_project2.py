#number guessing game in python

import random
import math
lower_num  = int(input("enter the number to start start  : "))
upper_num = int(input("enter the number for end : "))

random_num = random.randint(lower_num , upper_num)
print("\n\t you have only ",round(math.log(upper_num-lower_num +1,2)), "round to guess the integer !!\n")

count =0
while count < math.log(upper_num-lower_num +1,2):
    count += 1
    guess_num = int(input("guess the number "))
    if guess_num == random_num:
        print("congratulations you did it in your ",count ," try!!")
        break
    elif guess_num < random_num:
        print("you choose very small number !! try again")
    elif guess_num > random_num:
        print("you choose very big  number !! try again")
if count >= math.log(upper_num-lower_num +1, 2):
    print("\t better luck next time !!")
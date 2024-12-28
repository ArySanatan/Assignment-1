# Q2. Write a Python program that checks a number divisible by 3 and 2.

Num=int(input("Enter Number : ")) 

if(Num%3==0):
    if(Num%2==0): print(Num,"is divisible by 3 and 2")
    else: print(Num,"is not divisible by 3 and 2")
    
else: print(Num,"is not divisible by 3 and 2")

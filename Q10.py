'''Q10. Write a Python program that checks whether a question is Hard or Easy. A
problem is easy only if all 4 members say it is easy. (Chocolate Question)
Example:
Input : 0 0 0 1 → 0 means easy and 1 means hard. So, since one of them said it is
hard. Then it is a hard problem. Print “Hard”
Input: 0 0 0 0 → Since, everyone said it was an easy question. Print “Easy”
Take input in the same format as mentioned above.'''

print("Enter Inputs - \n0 means Question is Easy\n1 means Question is Hard\n")

#taking user inputs from 4 members
mem_1=int(input("Member 1 : "))
mem_2=int(input("Member 2 : "))
mem_3=int(input("Member 3 : "))
mem_4=int(input("Member 4 : "))

if ((mem_1==0 or mem_1==1)and
    (mem_2==0 or mem_2==1)and
    (mem_3==0 or mem_3==1)and
    (mem_4==0 or mem_4==1)):
        if (mem_1==mem_2==mem_3==mem_4==0): print("Easy")
        else: print("Hard")
    
else: print("Invalid Inputs")
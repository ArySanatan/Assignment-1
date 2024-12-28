'''Q7. Write a Python program that takes 3 number and print the second largest
number.'''

Num_1 = int(input("Enter 1st Number : "))
Num_2 = int(input("Enter 2nd Number : "))
Num_3 = int(input("Enter 3rd NUmber : "))

if (((Num_1 > Num_2) and (Num_1 < Num_3))or((Num_1 < Num_2) and (Num_1 > Num_3))): print(Num_1,"is Second Largest")
elif (((Num_2 > Num_1) and (Num_2 < Num_3))or((Num_2 < Num_1) and (Num_2 > Num_3))): print(Num_2,"is Second Largest")
elif (((Num_3 > Num_1) and (Num_3 < Num_2))or((Num_3 < Num_1) and (Num_3 > Num_2))): print(Num_3,"is Second Largest")
else: print("All are same")
'''Q3. Write a Python program that takes the length of sides as input and checks
whether a triangle can be formed.'''

#taking user inputs for three sides of triangle
side_a=int(input('Enter side a : '))
side_b=int(input('Enter side b : '))
side_c=int(input('Enter side c : '))

#conditons using logical and
if ((side_a + side_c > side_b) and (side_c+side_b>side_a) and (side_a + side_b > side_c)): print("Triangle can be formed")
else:print("Triangle cannot be formed")  
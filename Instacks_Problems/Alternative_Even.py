
# Write a program to print all alternative even numbers 
# in the given range if no numbers then print NO NUMBERS 
# if starting range is greater than ending range print INVALID INPUTS


# Example:
# Input  :           10

#                        30

# Output :        10 14 18 22 26 30


# Explanation:
# int the above example we have to print all the alternative even numbers in the range of 10 to 30 they are 10 14 18 22 26 30

# ------------------------------------- O ----------------------------------------------------

# Solution - I

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("INVALID INPUTS")

else:
    alternative = 0
    flag = False
    
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            alternative += 1
            flag = True
            
            if alternative % 2 != 0:
                print(i, end =" ")
    if not flag:
        print("NO NUMBERS")

# ----------------------------------------------- O --------------------------------------------

# Description:
# Write a Program to Print the Alternative Even Numbers Between the Given Numbers?


# Example:
# Input 1    :  10

#                    30

# Output 1 :  12 16 20 24 28

 

# Input 2    :  5

#                    25

# Output 2 :  6 10 14 18 22 

 

# Input 3     :  -5

#                     25

# Output 3  :  Invalid Inputs


# Solution - I

n1 = int(input())
n2 = int(input())

if n1<=0 or n2<=0:
    print("Invalid Inputs")

else:
    alt_even = 0
    flag = False
    
    for i in range(n1 +1,n2):
        if i % 2 == 0:
            alt_even += 1
            flag = True
            
            if alt_even % 2 != 0:
                print(i, end=" ")
    
    

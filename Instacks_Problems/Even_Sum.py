
# Write a program to print sum of all even numbers in between 
# the Given Numbers if no even numbers print NO NUMBERS
# if starting range is greater than ending range then print INVALID RANGE

# Example:
# Input :          20

#                  40

# Output :       270


# Explanation:
# in the above example we have to sum all the even numbers in between 20 and 40

# 22+24+26+28+30+32+34+36+38=270

# ----------------------------------------- O ------------------------------------------

# Solution

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("INVALID RANGE")

else:
    even_sum = 0
    flag = False
    
    for i in range(n1 + 1, n2):
        if i % 2 == 0:
            even_sum += i
            flag = True
    
    if not flag:
        print("NO NUMBERS")
    else:
        print(even_sum)

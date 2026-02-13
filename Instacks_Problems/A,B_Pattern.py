# Description:
# Write a program to print A,B in given number of times alternatively


# Constraints:
# Input :          First line of input contains Integer n 

# Output :       Print A,B for n no of times


# Example:
# Input :          5

# Output :       A,B,A,B,A,B,A,B,A,B

# --------------------------- O ----------------------------------

# Solution

n1 = int(input())

L1 = "A,B," * n1
print(L1[:-1])
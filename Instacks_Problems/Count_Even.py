# Description:
# Write a program to find the count of even numbers in given range.
# if no even numbers print NO NUMBERS if Strating range is greater than ending range print INVALID RANGE


# Example:
# Input :      10

#                   20

# Output :   6


# Explanation:
# In the above example there are 6(including 10,20)
# even numbers in range of 10 and 20 are 10,12,14,16,18,20

# Solution

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("INVALID RANGE")

else:
    
    count = 0
    
    for i in range(n1,n2 + 1):
        if i % 2 == 0:
            count +=1
    print(count)
            
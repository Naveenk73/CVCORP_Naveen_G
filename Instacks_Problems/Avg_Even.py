# Description:
# Write a program to find the average of all even numbers in the given range.
# if the strating range is Greater than ending range then print 

# "INVALID RANGE"
 
# Example:
# Input :         10

#                      30

# Output :       20.0


# Explanation:
# in the above example even numbers in range are 10,12,14,16,18,20,22,24,26,28,30

# avarage of those numbers is 20.0

# Solution

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("INVALID RANGE")
    
else:
    
    L1 = []
    for i in range(n1,n2 +1):
        if i % 2 == 0:
            L1.append(i)
    
    avg = sum(L1) / len(L1)
    print(float(avg))

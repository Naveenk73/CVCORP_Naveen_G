# Description:
# Write a program to print all Odd Numbers in Given Range.
# if starting range is greater than ending range print "INVALID RANGE"

# Example:
# Input :            1

#                        10

# Output :         1 3 5 7 9


# Explanation:
# in the above example you have to print all the odd numbers in range of 1 to 10 they are 1 3 5 7 9

# Solution


n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("INVALID RANGE")

else:
    
    for i in range(n1,n2):
        if i % 2!=0:
            print(i, end=" ")

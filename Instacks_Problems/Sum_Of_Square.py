# Description:
# Write a program to print sum of squares of the numbers in given range.
# if starting range is Greater than ending range print "INVALID RANGE"


# Example:
# Input :          5 

#                      23

# Output :       4294


# Explanation:
# Input :        5 

#                    23

# Output :     4294

# Explanation :

# 5**2 + 6**2 + 7**2 + 8**2 + 9**2 + 10**2 + 11**2 + 12**2 + 13**2 
# + 14**2 + 15**2 + 16**2 + 17**2 + 18**2 + 19**2 + 20**2 + 21**2 + 22**2 + 23**2

# =25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 + 169 + 196 + 225 + 256 + 289 + 324 + 361 + 400 + 441 + 484 + 529

# =4294

# Solution

n1 = int(input())
n2 = int(input())

if n1 > n2:
    print("INVALID RANGE")

else:
    
    total = 0
    
    for i in range(n1,n2+1):
        total += i**2
    print(total)



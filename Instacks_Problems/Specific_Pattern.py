# Description:
# Write a program to print following pattern 

# if input is 10 and -5

# output will be 10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6

 
# Example:
#  Input :            10   

#                         -5

# Output :         10@9,9@8,8@7,7@6,6@5,5@4,4@3,3@2,2@1,1@0,0@-1,-1@-2,-2@-3,-3@-4,-4@-5,-5@-6

# Solution

n1 = int(input())
n2 = int(input())

L1 = ""

if n1 > n2:
    for i in range(n1,n2-1, -1):
        L1 += f"{i}@{i-1},"
    print(L1[:-1], end="")
    
else:
    for i in range(n1,n2+1):
        L1 += f"{i}@{i+1},"
    print(L1[:-1], end="")
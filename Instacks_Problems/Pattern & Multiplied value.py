# Description:
# Write a Program to Print the following series 2*3,3*4,4*5,......16*17  
# (Print in two ways – Pattern & Multiplied value) .

# Example:
# Input 1    :    2

#                      16

# Output 1 :    2*3, 3*4, 4*5, 5*6, 6*7, 7*8, 8*9, 9*10, 10*11, 11*12, 12*13, 13*14, 14*15, 15*16, 16*17

#                      6, 12, 20, 30, 42, 56, 72, 90, 110, 132, 156, 182, 210, 240, 272

 

# Input 2    :    10

#                       1

# Output 2 :    1*2, 2*3, 3*4, 4*5, 5*6, 6*7, 7*8, 8*9, 9*10, 10*11

#                       2, 6, 12, 20, 30, 42, 56, 72, 90, 110

# --------------------------------- O -----------------------------------------

# Solutiion

n1 = int(input())
n2 = int(input())

L1 = ""
L2 = ""

for i in range(n1,n2+1):
    L1 += f"{i}*{i+1}, "
    L2 += f"{i*(i+1)}, "
print(L1[:-2])
print(L2[:-2])

# Sample Input 0
# x = 1
# y = 1
# z = 1
# n = 2
# Print an array of the elements that do not sum to 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
#
x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

# Doubt
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# if x + y + z != n:
#     for i, j, k in range(x, y, z):
#         print([i, j, k], end=" ")









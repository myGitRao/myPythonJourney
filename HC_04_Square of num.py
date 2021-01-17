# The list of non-negative integers that are less than n=3 is [0,1,2]
# Print the square of each number on a separate line
# 0
# 1
# 4

if __name__ == '__main__':
    n = int(input())
if n <= 0:
    print("0")
else:
    for i in range(0, n):
        print(i * i)

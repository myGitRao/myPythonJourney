# Sample Input
# 5
# Sample Output
# 1
# 22
# 333
# 4444

n = int(input("n : "))
for i in range(1, n + 1) :
    print(i * ((10 ** i) // 9))

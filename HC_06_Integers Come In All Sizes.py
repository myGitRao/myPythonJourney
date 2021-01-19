# Sample Input
# 9
# 29
# 7
# 27
# Sample Output
# 4710194409608608369201743232
# Note: This result is bigger than . Hence, it won't fit in the long long int of C++ or a 64-bit integer.

a = int(input("a : "))
b = int(input("b : "))
c = int(input("c : "))
d = int(input("d : "))

print((a**b) + (c**d))
print(pow(a,b) + pow(c,d))
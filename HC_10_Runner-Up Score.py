# Sample Input 0
# 5
# 2 3 6 6 5
# Sample Output 0
# 5
lst = []
lst2 = []
n = int(input("Enter the number of scores to be displayed : "))
for i in range(0, n):
    scores = int(input())
    lst.append(scores)
    lst.sort()
# uniq = int((set(lst)))
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'

uniq = set(lst)
# print(type(uniq))
# print(uniq[-2]) # TypeError: 'set' object is not subscriptable

uniq.remove(max(uniq))
print(max(uniq))

# Can also sort unique values through the append method
# for i in lst:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)





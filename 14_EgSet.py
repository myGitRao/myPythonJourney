s = set()
print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
print(s)
s.remove(2)
s1 = {4, 6}
print(s.isdisjoint(s1)) # The isdisjoint() method returns True
# if none of the items are present in both sets, otherwise it returns False.


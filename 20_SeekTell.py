# Seek and tell functions in python

f = open("Food1.txt")
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readlines())
f.seek(0)
print(f.tell())
print(f.readline())
f.close()


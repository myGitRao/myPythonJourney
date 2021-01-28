# In Python, its try & except , in other languages its try & catch
# Eg : Used in internet related programs, if some data is been fetched from internet
# and you internet connectivity is down in such cases try and except plays an important role
# for continuation of program


a = input("First Number: ")
b = input("Second Number: ")
try:
    addition = int(a)+int(b)
    print(addition)
except Exception as e:
    print(e)

print("This is an very important line to be printed after exception occurs")
# Faulty Calculator
# INPUT:: The user will provide the following inputs:
# Operator
# The two numbers, between which the operator is applied
# OUTPUT :: All the results will be correct, except for these few:
# 45 * 3 = 555
# 56+9 = 77
# 56/6 = 4

a = int(input("a: "))
b = int(input("b: "))
operator = input("""
Select operator from the below options:
+
-
*
/
operator: """)
if operator == "*":
    if a == 45 and b == 3:
        print("45 * 3 = 555")
    else:
        print("{} * {} = ".format(a,b), a*b)
elif operator == "+":
    if a == 56 and b == 9:
        print("56 + 9 = 77")
    else:
        print("{} + {} = ".format(a, b), a + b)
elif operator == "-":
    print("{} - {} = ".format(a, b), a - b)
elif operator == "/":
    if a == 56 and b == 6:
        print(" 56 / 6 = 4")
    else:
        print("{} / {} = ".format(a, b), a / b)







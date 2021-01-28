# Take input from user until he/she enters something above 100

number = int(input("Enter a number: "))
while True :
    if number < 100:
        number = int(input("Enter the number: "))
        continue
    else:
        print("Congratulations you have entered a number greater or equal to 100")
        break

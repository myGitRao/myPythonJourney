# Opening a file
fPointer = open("Food.txt")
val = fPointer
print(val)

# Reading the file
value = fPointer.read()
print(value)

# closing the opened file
fPointer.close()

# Opening and reading line by line
f = open("Food.txt", "rt")
print(f.readlines())  # Reads all the lines
print(f.readline())  # Reads a single line
f.close()

# Open a file and do modifications

p = open("Food.txt", "w")
p.write("Inserting this in a file with write mode")
p.close()

p = open("Food.txt")
print(p.readlines())
p.close()

# Creating a new file
f = open("Food1.txt", "w")
f.write("I like Apples\n")

f=open("Food1.txt", "r")
print(f.readlines())
f.close()

# Appending in a file
f = open("Food1.txt","a")
f.write("I also love oranges\n")
a = f.write("I also love grapes\n")
print(a)            # how many characters are their in the file
f.close()

# Read and write modes together
f =open("Food1.txt", "r+")
print(f.read())
f.write("I am in writing mode now")
f.close()
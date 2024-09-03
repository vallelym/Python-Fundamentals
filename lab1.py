#Part One
print("Hello World")

#Part Two
username= 'Bob'
age= 32
print(username, ' is ',age, ' years old')

#Part Two with Input
username=input('Please enter your name: ')
age = input ('Please enter your age: ')
print(username, 'is', age, 'years old')

#Part 3
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print("The perimeter of the rectangle is: {}".format(perimeter))
print("The area of the rectangle is: {}".format(area))

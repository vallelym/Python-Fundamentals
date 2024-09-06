#Part One
age = int(input('What is your age? '))
if age >= 18:
    print("You are in category A")
elif age >=16 and age< 18:
    print("You are in category B")
else:
    print("You are in category C")

#Part Two Exercise One
num1 = int(input("Chose your first number: "))
num2 = int(input("Chose your second number: "))

print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

calculator = input("Enter your choice (+, -, *, /): ")
if calculator == '+':
    result = num1 + num2
    print("The sum of {} and {} is: {}".format(num1, num2, result))
elif calculator == '-':
    result = num1 - num2
    print("The difference between {} and {} is: {}".format(num1, num2, result))
elif calculator == '*':
    result = num1 * num2
    print("The product of {} and {} is: {}".format(num1, num2, result))
elif calculator == '/':
    if num2 != 0:
        result = num1 / num2
        print("The quotient of {} and {} is: {}".format(num1, num2, result))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Incorrect Selection")
    
#Part Two Exercise Two
print ("Exam Grade Calculator")
print()
final_number = int(input("Enter the exam grade (1-100): "))
if final_number >= 71 and final_number <= 100:
    print("Destinction, Go and rule the World 👑")
elif final_number >= 61 and final_number <= 70:
    print("Merit, with great knowledge comes great responsibility 🦉.")
elif final_number >= 50 and final_number <= 60:
    print("Pass, a pass is a pass, well done 😂.")
elif final_number >= 1 and final_number <= 49:
    print("Fail, You shall not pass! 🧙‍♂️")
else:
  print("What are you talking about? 🤦‍♂️")

#Part Two Exercise Three
print ("Exam Grade Calculator")
print()

final_number = int(input("Enter the exam grade (1-100): "))
if final_number <1 or final_number >100:
    print("Invalid Input")
else:
    exam_level = int(input("Which exam level did you take (1 or 2)? "))
    if exam_level not in [1, 2]:
        print("Do you even attend this school? 🤦‍♂️")
    else:
        if exam_level == 1:
            if final_number >= 71 and final_number <= 100:
                print("Destinction, Go and rule the World 👑")
            elif final_number >= 61 and final_number <= 70:
                print("Merit, with great knowledge comes great responsibility 🦉.")
            elif final_number >= 50 and final_number <= 60:
                print("Pass, a pass is a pass, well done 😂.")
            elif final_number >= 1 and final_number <= 49:
                print("Fail, You shall not pass! 🧙‍♂️")
        elif exam_level == 2:
            if final_number >= 66 and final_number <= 100:
                print("Destinction, Go and rule the World 👑")
            elif final_number >= 51 and final_number <= 65:
                print("Merit, with great knowledge comes great responsibility 🦉.")
            elif final_number >= 40 and final_number <= 50:
                print("Pass, a pass is a pass, well done 😂.")
            elif final_number >= 1 and final_number <= 40:
                print("Fail, You shall not pass! 🧙‍♂️")

#Part Two Exercise Three

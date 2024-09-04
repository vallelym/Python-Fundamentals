# Part One
number = 1
while number <=100:
    square = number ** 2
    print(f"Number: {number}, Square: {square}")
    if square > 2000:
        break
    number += 1

# Part Two
factorial = 1
counter = 1

number = int(input("Please enter an integer: "))
while counter <= number:
    factorial *= counter
    counter += 1

print(f"The factorial of {number} is {factorial}")

#Part Three
target = 1000
initial = float(input("What is the value of your initial investment: "))
interest_rate = 10
years = 0

while initial < target:
    initial *= (1 + interest_rate / 100)
    years += 1

print(f"It will take {years} years for the investment to grow to £1000.")

# Part Four
min_value = 1
max_value = 100
attempts = 0

while attempts < 3:
        user_input = int(input(f"Please enter an integer between {min_value} and {max_value}: "))
        if min_value <= user_input <= max_value:
            print(f"Valid value entered: {user_input}")
            break
        elif min_value <= user_input >= max_value:
            print(f"Value not within the range {min_value} to {max_value}. Try again.")
        
        attempts += 1

if attempts == 3:
    print(None)

#Part Five
vowels = "aeiouAEIOU"
word = input("Enter a word: ")
counter = 0
index = 0

while index < len(word):
    if word[index] in vowels:
        counter += 1
    index += 1

print(f"The number of vowels in the word '{word}' is {counter}.")

#Part Six
def calculate_average(marks):
    return sum(marks) / len(marks)

def get_mark(subject):
    while True:
        try:
            mark = int(input(f"Enter the mark for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid mark. Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    subjects = ["Math", "English", "ICT"]
    marks = []

    for subject in subjects:
        mark = get_mark(subject)
        marks.append(mark)

    average_mark = calculate_average(marks)
    result = "Pass" if average_mark >= 65 else "Fail"

    print(f"\nAverage mark: {average_mark:.2f}")
    print(f"Overall result: {result}")

if __name__ == "__main__":
    main()

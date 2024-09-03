#Task 1
# def weight_converter():
#    try:
#        weight = float(input("Enter the weight: "))
#        unit = input("Is the weight in (K)gs or (L)bs? ").strip().lower()
#
#        if unit == 'k':
#            converted_weight = weight * 2.20462
#            print(f"{weight} Kgs is equal to {converted_weight:.2f} Lbs.")
#        elif unit == 'l':
#            converted_weight = weight / 2.20462
#            print(f"{weight} Lbs is equal to {converted_weight:.2f} Kgs.")
#        else:
#            print("Invalid unit. Please enter 'K' for Kgs or 'L' for Lbs.")
#    except ValueError:
#        print("Invalid input. Please enter a numeric value for the weight.")
#
#if __name__ == "__main__":
#    weight_converter()

#Task 2
#num = 30
#num1 = 40

#largest = (num + num1 + abs(num - num1)) // 2
#print (largest)

#Task 3
#While Loop
names = ["Mitchell", "Bobby", "Charlie", "Elliott", "Fianna"]
i = 0
while i < len(names):
    print(f"{names[i]} is Awesome!")
    i += 1

#For Loop
names = ["Mitchell", "Bobby", "Charlie", "Elliott", "Fianna"]
for name in names:
    print(f"{name} is Awesome!")

#List Comprehension
names = ["Mitchell", "Bobby", "Charlie", "Elliott", "Fianna"]
awesome_names = [f"{name} is Awesome!" for name in names]
for awesome_name in awesome_names:
    print(awesome_name)

#One-line List Comprehension
names = ["Mitchell", "Bobby", "Charlie", "Elliott", "Fianna"]
[print(f"{name} is Awesome!") for name in names]

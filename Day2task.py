def weight_converter():
    try:
        weight = float(input("Enter the weight: "))
        unit = input("Is the weight in (K)gs or (L)bs? ").strip().lower()

        if unit == 'k':
            converted_weight = weight * 2.20462
            print(f"{weight} Kgs is equal to {converted_weight:.2f} Lbs.")
        elif unit == 'l':
            converted_weight = weight / 2.20462
            print(f"{weight} Lbs is equal to {converted_weight:.2f} Kgs.")
        else:
            print("Invalid unit. Please enter 'K' for Kgs or 'L' for Lbs.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the weight.")

if __name__ == "__main__":
    weight_converter()

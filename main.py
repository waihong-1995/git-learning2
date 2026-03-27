#Basic BMI calculator program using structural programming method - v1.0
def get_height():
    while True:
        try:
            height_cm = float(input("Enter your height (in cm): "))
            
            # reasonable human range: 50 cm to 300 cm
            if 50 <= height_cm <= 300:
                return height_cm
            else:
                print("Height must be between 50 cm and 300 cm. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight (in kg): "))
            
            # reasonable range: 2 kg to 500 kg
            if 2 <= weight <= 500:
                return weight
            else:
                print("Weight must be between 2 kg and 500 kg. Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# main program
height = get_height()
weight = get_weight()

bmi = calculate_bmi(weight, height)
category = classify_bmi(bmi)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Category: {category}")
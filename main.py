#Basic BMI calculator program using structural programming method - v1.0
def calculate_bmi(weight, height_cm):
    return weight / ((height_cm / 100) ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    height = float(input("Enter your height (in cm): "))
    weight = float(input("Enter your weight (in kg): "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
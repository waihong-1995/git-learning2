from app.bmi import calculate_bmi, classify_bmi


def main():
    height = float(input("Enter your height (in cm): "))
    weight = float(input("Enter your weight (in kg): "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
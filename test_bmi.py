from main import calculate_bmi, classify_bmi


def test_bmi_value():
    assert round(calculate_bmi(70, 170), 2) == 24.22


def test_category():
    assert classify_bmi(24.22) == "Healthy"
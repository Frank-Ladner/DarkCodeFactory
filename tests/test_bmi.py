from math import isclose

from app.bmi import calculate_bmi, classify_bmi


def test_calculate_bmi():
    assert isclose(calculate_bmi(170, 70.0), 24.22145, rel_tol=0.00001)


def test_classify_bmi():
    cases = [
        (18.4, "Untergewicht", "blue"),
        (18.5, "Normalgewicht", "green"),
        (24.9, "Normalgewicht", "green"),
        (25.0, "Übergewicht", "orange"),
        (29.9, "Übergewicht", "orange"),
        (30.0, "Adipositas", "red"),
    ]

    for bmi, expected_category, expected_color in cases:
        assert classify_bmi(bmi) == (expected_category, expected_color)

import pytest

from app.bmi import calculate_bmi, classify_bmi


def test_calculate_bmi():
    assert calculate_bmi(170, 70.0) == pytest.approx(24.22145)


@pytest.mark.parametrize(
    ("bmi", "expected_category", "expected_color"),
    [
        (18.4, "Untergewicht", "blue"),
        (18.5, "Normalgewicht", "green"),
        (24.9, "Normalgewicht", "green"),
        (25.0, "Übergewicht", "orange"),
        (29.9, "Übergewicht", "orange"),
        (30.0, "Adipositas", "red"),
    ],
)
def test_classify_bmi_boundaries(bmi, expected_category, expected_color):
    assert classify_bmi(bmi) == (expected_category, expected_color)

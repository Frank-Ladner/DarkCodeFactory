def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Untergewicht", "blue"
    if bmi < 25:
        return "Normalgewicht", "green"
    if bmi < 30:
        return "Übergewicht", "orange"
    return "Adipositas", "red"

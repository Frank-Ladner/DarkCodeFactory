import streamlit as st

st.set_page_config(
    page_title="Dark Code Factory - BMI-Rechner",
    page_icon="🚀",
    layout="wide"
)

st.title("Dark Code Factory - BMI-Rechner")

st.write("Berechne deinen BMI (Body Mass Index)")

# Eingabefelder
col1, col2 = st.columns(2)

with col1:
    height_cm = st.number_input("Körpergröße (cm)", min_value=50, max_value=250, value=170, step=1)

with col2:
    weight_kg = st.number_input("Gewicht (kg)", min_value=10.0, max_value=500.0, value=70.0, step=0.1)

# Button zum Berechnen
if st.button("BMI berechnen"):
    # BMI-Berechnung: BMI = Gewicht (kg) / (Größe (m))²
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    # BMI-Kategorie bestimmen
    if bmi < 18.5:
        category = "Untergewicht"
        color = "blue"
    elif bmi < 25:
        category = "Normalgewicht"
        color = "green"
    elif bmi < 30:
        category = "Übergewicht"
        color = "orange"
    else:
        category = "Adipositas"
        color = "red"
    
    # Ergebnisse anzeigen
    st.metric("Dein BMI", f"{bmi:.1f}")
    
    if color == "green":
        st.success(f"Kategorie: {category} ✓")
    elif color == "blue":
        st.info(f"Kategorie: {category}")
    elif color == "orange":
        st.warning(f"Kategorie: {category}")
    else:
        st.error(f"Kategorie: {category}")
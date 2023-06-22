import streamlit as st

# Define function to calculate the evaluation of acid base disorders
def calculate_disorder(pH, HCO3, Na, Cl):
    anion_gap = Na - (Cl + HCO3)
    if pH < 7.35 and anion_gap > 12:
        return "High anion gap metabolic acidosis"
    elif pH < 7.35 and anion_gap <= 12:
        return "Normal anion gap (hyperchloremic) metabolic acidosis"
    
    return "No metabolic acidosis detected"

# Title of the app
st.title("Evaluation of Metabolic Acidosis using Anion Gap")

# User inputs
st.markdown("## Input Parameters")
st.markdown("Please enter the following laboratory measurements:")

pH = st.number_input('pH (Normal range: 7.35-7.45)', min_value=0.0, max_value=14.0)
HCO3 = st.number_input('HCO3 in mEq/L (Normal range: 22-28 mEq/L)', min_value=0.0)
Na = st.number_input('Na in mEq/L (Normal range: 135-145 mEq/L)', min_value=0.0)
Cl = st.number_input('Cl in mEq/L (Normal range: 96-106 mEq/L)', min_value=0.0)

if st.button('Calculate'):
    result = calculate_disorder(pH, HCO3, Na, Cl)
    st.markdown("## Results")
    st.markdown("The result represents the probable primary acid-base imbalance based on the given parameters. Please consider further clinical and laboratory evaluation for accurate diagnosis.")
    st.write(f'The result is: **{result}**')

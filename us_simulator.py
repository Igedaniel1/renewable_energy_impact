import streamlit as st
import pandas as pd
import pickle

# ================================
# Load Trained Model & Label Encoder
# ================================
model = pickle.load(open("us_data_model.pkl", "rb"))

try:
    label_encoder = pickle.load(open("label_encoder.pkl", "rb"))
    decode_label = True
except FileNotFoundError:
    decode_label = False

# ================================
# Energy Feature Emission Factors
# ================================
emission_factors = {
    'Geothermal Energy': 0.7,
    'Solar Energy': 1.0,
    'Wind Energy': 1.2,
    'Waste Energy': 0.4,
    'Fuel Ethanol, Excluding Denaturant': 0.8,
    'Total Renewable Energy': 1.5,
    'Renewable Diesel Fuel': 0.85,
    'Other Biofuels': 0.75,
    'Conventional Hydroelectric Power': 0.55,
    'Biodiesel': 0.65
}

features = list(emission_factors.keys())

# ================================
# Streamlit UI
# ================================
st.set_page_config(page_title="Sustainability Impact Simulator", layout="centered")
st.title("🌍 Sustainability Impact Simulator")
st.markdown("""
Simulate the environmental impact of different renewable energy usage patterns.
- 🧠 Predicts which sector your profile resembles.
- 🌱 Estimates CO₂ savings based on energy use.
""")

# Sidebar sliders for input
st.sidebar.header("🔧 Adjust Energy Usage")
inputs = {}
for feature in features:
    inputs[feature] = st.sidebar.slider(feature, 0.0, 100.0, 10.0, step=1.0)

input_df = pd.DataFrame([inputs])

# ================================
# Predict Sector
# ================================
prediction = model.predict(input_df)[0]
if decode_label:
    predicted_sector = label_encoder.inverse_transform([prediction])[0]
else:
    predicted_sector = f"Sector code {prediction}"

# ================================
# Calculate CO₂ Savings
# ================================
co2_savings = sum(inputs[feat] * emission_factors[feat] for feat in features)

# ================================
# Show Results
# ================================
st.subheader("🧠 Predicted Sector")
st.success(predicted_sector)

st.subheader("🌱 Estimated CO₂ Savings")
st.metric(label="Estimated CO₂ Saved (kg)", value=round(co2_savings, 2))

# ================================
# CO₂ Breakdown Chart
# ================================
st.subheader("📊 CO₂ Savings by Energy Type")
savings_breakdown = {feat: inputs[feat] * emission_factors[feat] for feat in features}
savings_df = pd.DataFrame.from_dict(savings_breakdown, orient='index', columns=['CO₂ Saved (kg)'])
st.bar_chart(savings_df)

# Optional Note
st.caption("Emission factors are illustrative. Actual savings vary by efficiency and location.")

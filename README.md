# 🌱 Renewable Energy Sector Classifier & Emission Impact Estimator

This project uses machine learning to classify U.S. renewable energy consumption patterns into economic sectors (e.g., Commercial, Industrial, Electric Power) and estimates the **carbon emissions avoided** due to renewable energy usage.

Built with the goal of supporting researchers and policymakers, this tool offers both predictive power and environmental impact insights — all through an intuitive, interactive web interface.

---

## 🚀 Project Highlights

- **Classification Model:** Predicts the sector of renewable energy consumption using real-world U.S. energy data.
- **Emission Simulation:** Calculates potential CO₂ emissions offset based on energy consumption and emission factors.
- **Interactive Web App:** Built using Streamlit for quick, meaningful insights.

---

## 🧠 Machine Learning Overview

- **Dataset:** U.S. Renewable Energy Consumption data (by energy type and sector)
- **Target Variable:** `Sector` (Commercial, Industrial, Transportation, Electric Power)
- **Features:** Includes 14+ renewable sources such as:
  - Hydroelectric Power
  - Geothermal Energy
  - Solar Energy
  - Wind Energy
  - Biodiesel, Biofuels, and more
- **Model Used:** LogisticRegression
- **Performance:** Achieved **99% accuracy**

---

## 📊 Emission Impact Estimation

After classification, the app multiplies each renewable energy source by its corresponding CO₂ **emission factor** (in kg CO₂ per BBTU) to estimate total emissions **avoided** through renewable use.

---

## 💻 Tech Stack

- **Python**
- **Scikit-learn**
- **Pandas / NumPy**
- **Matplotlib / Seaborn**
- **Streamlit** (for interactive UI)
- **Link** (https://igedaniel1-renewable-energy-impact-us-simulator-5qxcho.streamlit.app)
---

## 🖥️ Running the App Locally

### 1. Clone the repo

```bash
git clone https://github.com/Igedaniel1/renewable_energy_impact.git
cd renewable_energy_impact

pip install -r requirements.txt

streamlit run us_simulator.py





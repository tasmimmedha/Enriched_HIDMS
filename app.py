"""HIDMS — Interactive Diabetes-Risk Demo (Streamlit).

Run with:

    pip install streamlit
    streamlit run app.py

Adjust the sliders to a patient's measurements and the model predicts the
diabetes-risk level in real time.

⚠️  Demo only — model trained on simulated data, not for clinical use.
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from hidms.demo import predict_risk, load_model

st.set_page_config(page_title="HIDMS Demo", page_icon="🩺", layout="centered")

LEVEL_COLORS = {"Low": "#2a9d8f", "Moderate": "#e9c46a", "High": "#e76f51"}


@st.cache_resource
def get_model():
    return load_model()


st.title("🩺 HIDMS — Diabetes Risk Demo")
st.caption(
    "AI-powered preventive healthcare thesis demo · model trained on **simulated** data — "
    "educational use only, not a medical device."
)

with st.sidebar:
    st.header("Patient measurements")
    age = st.slider("Age (years)", 20, 85, 45)
    sex = st.radio("Sex", ["female", "male"], horizontal=True)
    height_m = st.number_input("Height (m)", 1.40, 2.00, 1.65, step=0.01)
    weight_kg = st.number_input("Weight (kg)", 40.0, 140.0, 70.0, step=1.0)
    st.divider()
    systolic_bp = st.slider("Systolic BP (mmHg)", 90, 200, 120)
    diastolic_bp = st.slider("Diastolic BP (mmHg)", 55, 130, 80)
    fasting_glucose = st.slider("Fasting glucose (mg/dL)", 65, 300, 95)
    st.divider()
    total_cholesterol = st.slider("Total cholesterol (mg/dL)", 120, 320, 190)
    hdl = st.slider("HDL (mg/dL)", 20, 100, 50)
    ldl = st.slider("LDL (mg/dL)", 50, 240, 110)
    triglycerides = st.slider("Triglycerides (mg/dL)", 40, 600, 130)
    st.divider()
    smoker = st.checkbox("Smoker")
    physical_activity = st.checkbox("Physically active", value=True)
    family_history = st.checkbox("Family history of diabetes")

patient = {
    "age": age,
    "sex": sex,
    "height_m": height_m,
    "weight_kg": weight_kg,
    "systolic_bp": systolic_bp,
    "diastolic_bp": diastolic_bp,
    "fasting_glucose": fasting_glucose,
    "total_cholesterol": total_cholesterol,
    "hdl": hdl,
    "ldl": ldl,
    "triglycerides": triglycerides,
    "smoker": smoker,
    "physical_activity": physical_activity,
    "family_history": family_history,
}

result = predict_risk(get_model(), patient)
risk = result["risk"]
level = result["level"]

bmi = weight_kg / height_m**2

col1, col2, col3 = st.columns(3)
col1.metric("BMI", f"{bmi:.1f}")
col2.metric("Predicted risk", f"{risk * 100:.1f}%")
col3.metric("Risk level", level)

st.progress(risk, text=f"Estimated diabetes risk: {risk * 100:.1f}%")

st.markdown(
    f"<div style='padding:1rem;border-radius:0.5rem;background:{LEVEL_COLORS[level]}22;"
    f"border:1px solid {LEVEL_COLORS[level]};color:#333'>"
    f"<b>🩺 Interpretation:</b> {result['message']}</div>",
    unsafe_allow_html=True,
)

fig_path = Path("reports/figures/demo_feature_importance.png")
if fig_path.exists():
    with st.expander("🔍 What drives the prediction?"):
        st.image(str(fig_path), caption="Feature importance from the trained Random Forest")

st.divider()
st.caption(
    "Built with `src/hidms` — synthetic data generator, scikit-learn pipeline, "
    "and evaluation module. See `scripts/train_demo.py` to retrain."
)

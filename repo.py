import streamlit as st

st.set_page_config(
    page_title="Diabetic Foot Monitor",
    page_icon="🦶"
)

st.title("🦶 Diabetic Foot Monitoring System")
st.write("Smart monitoring for early foot-ulcer risk detection")

st.sidebar.header("Patient Details")

name = st.sidebar.text_input("Patient Name", "Patient")
age = st.sidebar.number_input("Age", 1, 100, 50)

st.header("Sensor Readings")

pressure = st.slider(
    "Foot Pressure",
    min_value=0,
    max_value=100,
    value=40
)

temperature = st.slider(
    "Foot Temperature (°C)",
    min_value=20.0,
    max_value=45.0,
    value=32.0
)

movement = st.slider(
    "Movement Level",
    min_value=0,
    max_value=100,
    value=40
)

st.subheader("Monitoring Results")

col1, col2, col3 = st.columns(3)

col1.metric("Pressure", f"{pressure}%")
col2.metric("Temperature", f"{temperature} °C")
col3.metric("Movement", f"{movement}%")

# Simple demonstration risk calculation
risk_score = 0

if pressure > 70:
    risk_score += 2
elif pressure > 50:
    risk_score += 1

if temperature > 37:
    risk_score += 2
elif temperature > 35:
    risk_score += 1

if movement > 80:
    risk_score += 1

st.subheader("Foot Risk Status")

if risk_score >= 4:
    st.error("🔴 HIGH RISK")
    st.warning("Abnormal readings detected. Please check the foot and seek medical advice.")

elif risk_score >= 2:
    st.warning("🟡 MEDIUM RISK")
    st.info("Monitor the foot closely and reduce excessive pressure.")

else:
    st.success("🟢 LOW RISK")
    st.info("Current readings are within the demonstration range.")

st.divider()

st.caption(
    "Prototype only — sensor thresholds must be clinically validated "
    "before use for medical decisions."
)

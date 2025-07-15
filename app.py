import streamlit as st
from health_data import simulate_data
from model import detect_anomalies
import altair as alt

st.set_page_config(page_title="AI Health Monitor", layout="wide")

st.title("🩺 AI-Powered Health Monitoring System")
st.markdown(
    "Monitoring real-time health to promote **SDG 3: Good Health & Well-being**.")

# Simulate and process data
df = simulate_data()
df = detect_anomalies(df)

# Metrics
latest = df.iloc[-1]
status_color = "red" if latest['anomaly'] == 'Anomaly' else "green"

col1, col2, col3 = st.columns(3)
col1.metric("❤️ Heart Rate", f"{latest['heart_rate']} bpm")
col2.metric("🩸 Blood Oxygen", f"{latest['blood_oxygen']}%",
            delta="Healthy" if latest['blood_oxygen'] >= 95 else "Low")
col3.metric("⚠️ Status", latest['anomaly'],
            help="Detected by AI", delta_color=status_color)

st.markdown("### 📈 Health Trends Over Time")

chart = alt.Chart(df).mark_line().encode(
    x='timestamp:T',
    y='heart_rate',
    color='anomaly:N'
).properties(width=700, height=300)

st.altair_chart(chart, use_container_width=True)

st.markdown("### 🧠 Recommendations")
if latest['anomaly'] == 'Anomaly':
    st.error(
        "🚨 Anomaly detected in your vital signs. Please consult a healthcare provider.")
else:
    st.success("✅ All signs are normal. Keep up your healthy habits!")

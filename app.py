
import streamlit as st

st.set_page_config(
    page_title="Match Intelligence Pro V2",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 MATCH INTELLIGENCE PRO")
st.subheader("Multi-Sport Statistical Analytics")
st.caption("Version 2.0 | Local Development")

st.success("Your application is running successfully!")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sports Supported", "3")

with col2:
    st.metric("Prediction Engine", "READY")

with col3:
    st.metric("Database", "LOCAL")

st.divider()

st.header("Select Your Sport")

sport = st.selectbox(
    "Choose a sport",
    ["Cricket", "Football", "Tennis"]
)

st.info(f"You selected: {sport}")

st.subheader("System Information")

st.write("Python environment: Active")
st.write("Historical database: Prepared")
st.write("Statistical libraries: Installed")
st.write("Live data connection: Not connected")

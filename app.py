import pandas as pd
import openpyxl
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Bouncing Ball tracker",
    page_icon="🎱",
    layout="wide"
)

# Read data from CSV
df = pd.read_csv(
    filepath_or_buffer='simulation_data.csv',
    usecols=["Hour", "Soil Moisture", "Temperature", "Light Intensity"],
    nrows=1000
)

st.markdown(
    """
<style>
[data-testid="stMetricValue"] {
    font-size: 60px;
}
</style>
""",
    unsafe_allow_html=True,
)

moisture = df["Soil Moisture"]

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Mean Temperature:")
    #st.metric(label="df", value=f"{mean_temperature} {degree_sign}C", label_visibility="collapsed", delta=f"{difference} {degree_sign}C {temp}", delta_color="inverse")

l_delta = "Brighter than usual"
#if moisture<150:
#   l_delta = "Darker than usual (check light bulbs)"

with middle_column:
    st.subheader("Mean Light:")
    ##st.metric(label="ddd", label_visibility="collapsed", value=f"{mean_light}", delta=l_delta)

s_delta = "Louder than usual (check appliances)"
#if mean_sound<630:
##   s_delta = "Quieter than usual"

#with right_column:
#    st.subheader("Mean Sound:")
#    st.metric(label="d", label_visibility="collapsed", value=f"{mean_sound}", delta=s_delta, delta_color="inverse")

st.markdown("---")

graph = px.line(
    moisture,
    y="Soil Moisture",
    title="<i>Temperature (°C)</i><b> over time</b>",
    color_discrete_sequence=["#0083B8"] * len(moisture),
)
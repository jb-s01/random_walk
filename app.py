from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Public Equity Exploratory Data Analysis",
    layout="wide"
)

# Add Title
st.title("Public Equity Exploratory Data Analysis")

# Cache pygwalker renderer to manage memory usage
@st.cache_resource
def get_pyg_renderer() -> "StreamlitRenderer":
    df = pd.read_csv("./ATD.TO.csv")
    # If you want to use feature of saving chart config, set `spec_io_mode="rw"`
    return StreamlitRenderer(df, spec="./gw_config.json", spec_io_mode="rw")


renderer = get_pyg_renderer()

renderer.explorer()
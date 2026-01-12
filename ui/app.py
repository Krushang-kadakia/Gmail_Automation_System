import streamlit as st

st.set_page_config(page_title="Browser Agent", layout="centered")

st.title("Browser Automation Agent")
st.write("Phase 0.4 — UI is running")

if st.button("Test UI"):
    st.success("Streamlit is working correctly")

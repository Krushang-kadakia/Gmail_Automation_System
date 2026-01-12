import sys
from pathlib import Path
import asyncio
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from browser.controller import BrowserController

st.set_page_config(page_title="Browser Agent")

st.title("Browser Automation Agent — Phase 1")

url = st.text_input("Enter URL", "https://example.com")

if "browser" not in st.session_state:
    st.session_state.browser = BrowserController()

if st.button("Open Browser"):
    with st.spinner("Opening browser..."):
        result = asyncio.run(
            st.session_state.browser.open(url)
        )

    st.success("Browser opened")
    st.json(result)

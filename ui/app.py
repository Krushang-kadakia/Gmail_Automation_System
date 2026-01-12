import sys
from pathlib import Path
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from browser.controller import BrowserController
from utils.async_runner import AsyncRunner

st.set_page_config(page_title="Browser Agent")

st.title("Browser Automation Agent — Phase 1.1")

url = st.text_input("Enter URL", "https://example.com")

if "runner" not in st.session_state:
    st.session_state.runner = AsyncRunner()

if "browser" not in st.session_state:
    st.session_state.browser = BrowserController()

col1, col2 = st.columns(2)

with col1:
    if st.button("Open Browser"):
        with st.spinner("Opening browser..."):
            result = st.session_state.runner.run(
                st.session_state.browser.open(url)
            )
        st.success("Browser opened")
        st.json(result)

with col2:
    if st.button("Observe State"):
        with st.spinner("Reading browser state..."):
            state = st.session_state.runner.run(
                st.session_state.browser.observe()
            )
        st.info("Browser state observed")
        st.json(state)

st.divider()
st.subheader("Manual Actions")

action = st.selectbox(
    "Choose action",
    ["Click", "Type", "Wait", "Scroll"]
)

selector = st.text_input(
    "CSS Selector (for Click / Type)",
    placeholder="e.g. a, button#submit, input[name='q']"
)

text = st.text_input(
    "Text (for Type action)",
    placeholder="Text to type"
)

wait_ms = st.number_input(
    "Wait time (milliseconds)",
    min_value=100,
    value=1000,
    step=500
)

scroll_px = st.number_input(
    "Scroll pixels",
    min_value=100,
    value=500,
    step=100
)

if st.button("Execute Action"):
    with st.spinner("Executing action..."):
        if action == "Click":
            result = st.session_state.runner.run(
                st.session_state.browser.click(selector)
            )

        elif action == "Type":
            result = st.session_state.runner.run(
                st.session_state.browser.type_text(selector, text)
            )

        elif action == "Wait":
            result = st.session_state.runner.run(
                st.session_state.browser.wait(wait_ms)
            )

        elif action == "Scroll":
            result = st.session_state.runner.run(
                st.session_state.browser.scroll(scroll_px)
            )

    st.success("Action executed")
    st.json(result)

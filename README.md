# Browser Automation Agent

A modular, human-in-the-loop browser automation system built using **Python, Playwright, and Streamlit**, designed to evolve into a fully autonomous LLM-powered agent.

This project focuses on **system design, reliability, and agent architecture**, not just automation scripts.

---

## 🚀 Project Overview

The goal of this project is to build an **autonomous browser agent** that can:

1. Observe the current browser state
2. Decide the next action (via an LLM)
3. Execute the action in the browser
4. Validate results and log progress
5. Repeat the loop autonomously

The system is developed **phase by phase**, ensuring correctness and stability before introducing AI reasoning.

---

## 🧠 Current Status

✅ **Phase 1 Complete — Manual Agent (Human-in-the-Loop)**

The system currently supports:
- Opening and controlling a real browser
- Observing live browser state
- Executing deterministic browser actions
- Safe async execution integrated with a UI

LLM-based planning will be added in Phase 2.

---

## 🧩 Tech Stack

- **Python 3.12**
- **Playwright** – Reliable browser automation
- **Streamlit** – Interactive control UI
- **AsyncIO + background event loop** – Non-blocking execution
- **Ollama (DeepSeek R1)** – Local LLM reasoning *(next phase)*
- **Pandas + openpyxl** – Structured data & Excel output *(future)*

---

## 📁 Project Structure

browser-automation-agent/  
│  
├── browser/  
│ ├── controller.py # Browser actions & observation  
│ └── init.py  
│  
├── ui/  
│ ├── app.py # Streamlit UI  
│ └── init.py  
│  
├── utils/  
│ └── async_runner.py # Background async event loop  
│  
├── data/ # Generated outputs (gitignored)  
├── venv/ # Virtual environment (gitignored)  
│  
├── main.py  
├── requirements.txt  
└── README.md  

---

## 🏗️ Implemented Features (Phase 1)

### 🔹 Browser Control
- Open browser to any URL
- Persistent browser session

### 🔹 Browser State Observation
- Current URL
- Page title
- Truncated DOM snapshot

### 🔹 Manual Browser Actions
- Click elements via CSS selector
- Type text into inputs
- Scroll pages
- Wait for fixed durations

### 🔹 UI & Architecture
- Streamlit-based control panel
- Background async event loop to prevent deadlocks
- Modular, extensible design

---

## ▶️ How to Run

### 1. Create an Environment

```bash
python -m venv venv
```

### 2. Activate the Environment

```bash
venv/Scripts/activate #For windows
source venv/bin/activate #For Mac OS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 4. Start the UI

```bash
streamlit run ui/app.py
```
# DueDiligenceAI

A modular platform for simulating AI-based due diligence using LLMs like OpenAI and Anthropic. Pulls from multiple data sources, extracts insights, compares LLMs, and visualizes outputs in a dashboard.

## Features
- Upload or fetch financial/news/company data
- Summarize with both OpenAI and Anthropic models
- Compare outputs and hallucination risk
- Optional fine-tuning simulation
- Unified Streamlit dashboard

## Setup
```bash
pip install -r requirements.txt
```

## Run Dashboard
```bash
streamlit run dashboard.py
```

## API Keys
Use a `.env` file to store:
```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```